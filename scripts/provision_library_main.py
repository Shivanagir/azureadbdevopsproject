import argparse

from library_installer import install_jar_library

try:
    parser = argparse.ArgumentParser(
        description="Provisions JAR Library into a ADB Cluster")

    parser.add_argument("-1", "--WORKSPACE_BASE_URL",
                        help="Specify ADB Workspace Base URL")
    parser.add_argument("-2", "--BEARER_TOKEN", help="Specify Bearer Token")
    parser.add_argument("-3", "--CLUSTER_NAME",
                        help="Specify Cluster Name")
    parser.add_argument("-4", "--LIBRARY_PATH",
                        help="Specify Libary Path (JAR)")

    args = parser.parse_args()

    if not args.WORKSPACE_BASE_URL:
        print("Invalid Workspace Base URL Specified!")
        exit()

    if not args.BEARER_TOKEN:
        print("Invalid Bearer Token Specified!")
        exit()

    if not args.CLUSTER_NAME:
        print("Invalid Cluster Name Specified!")
        exit()

    if not args.LIBRARY_PATH:
        print("Invalid Library Path Specified!")
        exit()

    WORKSPACE_BASE_URL = args.WORKSPACE_BASE_URL
    BEARER_TOKEN = args.BEARER_TOKEN
    CLUSTER_NAME = args.CLUSTER_NAME
    LIBRARY_PATH = args.LIBRARY_PATH

    status = install_jar_library(
        WORKSPACE_BASE_URL, BEARER_TOKEN, CLUSTER_NAME, LIBRARY_PATH)

    if status:
        print("Library Installed Successfully into the Cluster ...")
    else:
        print("Unable to Install the Library ... Unknown Error")
except Exception as error:
    print("Error Occurred, Details : % s" % str(error))
