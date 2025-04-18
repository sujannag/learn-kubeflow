from helpers.KFPClientManager import KFPClientManager

# initialize a KFPClientManager
kfp_client_manager = KFPClientManager(
    api_url="http://localhost:8080/pipeline",
    skip_tls_verify=True,

    dex_username="user@example.com",
    dex_password="12341234",

    # can be 'ldap' or 'local' depending on your Dex configuration
    dex_auth_type="local",
)

# get a newly authenticated KFP client
# TIP: long-lived sessions might need to get a new client when their session expires
kfp_client = kfp_client_manager.create_kfp_client()

# test the client by listing experiments
experiments = kfp_client.list_experiments(namespace="kubeflow-user-example-com")
print(experiments)