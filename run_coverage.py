import os
import sys

# Expose vendor packages to PYTHONPATH
repo_dir = os.path.dirname(__file__)
package_dir = os.path.join(repo_dir, "pyblish_qml")
vendor_dir = os.path.join(package_dir, "vendor")
sys.path.insert(0, vendor_dir)


if __name__ == '__main__':
    import nose
    argv = sys.argv[:]
    argv.extend(['-c', '.noserc'])
    nose.main(argv=argv)
