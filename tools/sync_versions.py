"""Keeps apps.json in step with the real APKs.

For every app with an Android download, it downloads the APK, reads its package name and
version with aapt, and writes them into "package" and "version" (and "updated" when the version
changes). The App Bazaar Android app uses these to show Install, Update or Open.
"""
import datetime, glob, json, os, re, subprocess, sys, tempfile, urllib.request
from collections import OrderedDict

FILES = ["apps.json", "admin-apps.json"]


def aapt():
    tools = sorted(glob.glob(os.path.join(os.environ.get("ANDROID_HOME", "/usr/local/lib/android/sdk"), "build-tools", "*", "aapt")))
    if not tools:
        sys.exit("aapt not found")
    return tools[-1]


def badging(tool, url):
    with tempfile.NamedTemporaryFile(suffix=".apk") as f:
        req = urllib.request.Request(url, headers={"User-Agent": "app-bazaar-sync"})
        with urllib.request.urlopen(req, timeout=120) as r:
            f.write(r.read())
        f.flush()
        out = subprocess.run([tool, "dump", "badging", f.name], capture_output=True, text=True).stdout
    m = re.search(r"package: name='([^']+)'.*?versionName='([^']*)'", out)
    return (m.group(1), m.group(2)) if m else (None, None)


def main():
    tool = aapt()
    today = datetime.date.today().isoformat()
    for path in FILES:
        if not os.path.exists(path):
            continue
        with open(path) as f:
            data = json.load(f, object_pairs_hook=OrderedDict)
        changed = False
        for app in data.get("apps", []):
            url = (app.get("links") or {}).get("android")
            if not url or app.get("price") or app.get("example"):
                continue
            try:
                pkg, ver = badging(tool, url)
            except Exception as e:  # one broken link must not stop the others
                print(f"{app.get('id')}: {e}")
                continue
            if not pkg:
                print(f"{app.get('id')}: could not read the APK")
                continue
            print(f"{app.get('id')}: {pkg} {ver} (listed {app.get('version')})")
            if app.get("package") != pkg:
                app["package"] = pkg
                changed = True
            if ver and app.get("version") != ver:
                app["version"] = ver
                app["updated"] = today
                changed = True
        if changed:
            with open(path, "w") as f:
                f.write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
