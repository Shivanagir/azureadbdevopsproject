import argparse


def handle_arguments():
    parser = argparse.ArgumentParser(
        description="Provisions ADB Key Vaule backed Secret Scope")

    parser.add_argument("-1", "--TENANT_ID", help="Tenant ID")
    parser.add_argument("-2", "--AAD_APP_CLIENT_ID", help="AAD App Client ID")
    parser.add_argument("-3", "--AAD_APP_CLIENT_SECRET",
                        help="AAD App Client Secret")
    parser.add_argument("-4", "--AAD_USER_NAME", help="AAD User Name")
    parser.add_argument("-5", "--AAD_PASSWORD", help="AAD Password")
    parser.add_argument("-6", "--KV_RESOURCE_ID",
                        help="Azure Key Vault Resource ID")
    parser.add_argument("-7", "--KV_DNS", help="Azure Key Vault DNS Name")
    parser.add_argument("-8", "--ORGANIZATION_ID", help="ADB Organization ID")
    parser.add_argument("-9", "--ADB_RESOURCE_ID", help="ADB Resource ID")
    parser.add_argument("-10", "--ADB_BASE_URL", help="ADB Base URL")
    parser.add_argument("-11", "--SCOPE_NAME", help="Secret Scope Name")

    args = parser.parse_args()

    return args
