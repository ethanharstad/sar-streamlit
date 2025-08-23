import streamlit as st
from utils.auth import Auth
from config_file import Config

# ID of Secrets Manager containing cognito parameters
secrets_manager_id = Config.SECRETS_MANAGER_ID

# ID of the AWS region in which Secrets Manager is deployed
region = Config.DEPLOYMENT_REGION

# Initialise CognitoAuthenticator
authenticator = Auth.get_authenticator(secrets_manager_id, region)

# Authenticate user, and stop here if not logged in
is_logged_in = authenticator.login()
if not is_logged_in:
    st.stop()


def logout():
    authenticator.logout()


with st.sidebar:
    st.text(f"Welcome,\n{authenticator.get_username()}")
    st.button("Logout", "logout_btn", on_click=logout)

pg = st.navigation([
    st.Page("default_page.py", title="Default"),
    st.Page("kb_page.py", title="Knowledge Base"),
])
pg.run()
