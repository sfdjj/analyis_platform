# Created by wenchao.jia on 2018/11/20.
# Mail:wenchao.jia@qunar.com

SYSTEM_USER = 'System'

class Session:
    def __init__(self, tenant_id=SYSTEM_USER, current_user=SYSTEM_USER, system_app_code='', tx=None):
        self.tenant_id = tenant_id
        self.current_user = current_user
        self.system_app_code = system_app_code
        self.tx = tx
        self.request_time = None
        self.request_ip = None

class SessionSupporter:
    def __init__(self, session: Session):
        self.session = session
