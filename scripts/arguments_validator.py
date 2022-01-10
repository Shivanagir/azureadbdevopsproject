def validate_arguments(args):
    if not args.TENANT_ID:
        print("Invalid Tenant ID Specified!")
        exit()

    if not args.AAD_APP_CLIENT_ID:
        print("Invalid AAD Application ID Specified!")
        exit()

    if not args.AAD_APP_CLIENT_SECRET:
        print("Invalid AAD Application Client Secret Specified!")
        exit()

    if not args.AAD_USER_NAME:
        print("Invalid AAD User Name Specified!")
        exit()

    if not args.AAD_PASSWORD:
        print("Invalid AAD User Password Specified!")
        exit()

    if not args.KV_RESOURCE_ID:
        print("Invalid Azure Key Vault Resource ID Specified!")
        exit()

    if not args.KV_DNS:
        print("Invalid Azure Key Vault DNS Specified!")
        exit()

    if not args.ORGANIZATION_ID:
        print("Invalid Organization ID Specified!")
        exit()

    if not args.ADB_RESOURCE_ID:
        print("Invalid ADB Resource ID Specified!")
        exit()

    if not args.ADB_BASE_URL:
        print("Invalid ADB Base URL Specified!")
        exit()

    if not args.SCOPE_NAME:
        print("Invalid Secret Scope Specified!")
        exit()
