from arguments_parser import handle_arguments
from arguments_validator import validate_arguments
from token_generators import get_management_token, get_user_aad_token
from provision_kv_scope import provision_kv_secret_scope
try:
    args = handle_arguments()

    validate_arguments(args)

    TENANT_ID = args.TENANT_ID
    AAD_APP_CLIENT_ID = args.AAD_APP_CLIENT_ID
    AAD_APP_CLIENT_SECRET = args.AAD_APP_CLIENT_SECRET
    AAD_USER_NAME = args.AAD_USER_NAME
    AAD_PASSWORD = args.AAD_PASSWORD
    KV_RESOURCE_ID = args.KV_RESOURCE_ID
    KV_DNS = args.KV_DNS
    ORGANIZATION_ID = args.ORGANIZATION_ID
    ADB_RESOURCE_ID = args.ADB_RESOURCE_ID
    ADB_BASE_URL = args.ADB_BASE_URL
    SCOPE_NAME = args.SCOPE_NAME

    TOKEN_BASE_URL = 'https://login.microsoftonline.com/% s/oauth2/token' % TENANT_ID

    USER_AAD_TOKEN = get_user_aad_token(
        TOKEN_BASE_URL, AAD_APP_CLIENT_ID, AAD_USER_NAME, AAD_PASSWORD)

    if not USER_AAD_TOKEN:
        print("Unable to Retrieve the User AAD Token!")
    else:
        print("AAD User Token Successfully Generated ...")

    MANAGEMENT_TOKEN = get_management_token(
        TOKEN_BASE_URL, AAD_APP_CLIENT_ID, AAD_APP_CLIENT_SECRET)

    if not MANAGEMENT_TOKEN:
        print("Unable to Retrieve the Management Token")
    else:
        print("Management Token Generated Successfully ...")

    status = provision_kv_secret_scope(USER_AAD_TOKEN, MANAGEMENT_TOKEN, KV_RESOURCE_ID,
                                       KV_DNS, ORGANIZATION_ID, ADB_RESOURCE_ID, ADB_BASE_URL, SCOPE_NAME)

    if status:
        print("Provisioning AKV backed Secret Scope Successfully Completed ...")
except Exception as error:
    print("Error Occurred, % s" % str(error))
