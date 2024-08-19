# coding: utf-8
from sqlalchemy import Boolean, CHAR, Column, DateTime, ForeignKey, Integer, JSON, SmallInteger, String, Table, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base
from databaseConnection import Base

#Base = declarative_base()
metadata = Base.metadata


class AspNetRole(Base):
    __tablename__ = 'AspNetRoles'

    Id = Column(Text, primary_key=True)
    Name = Column(String(256))
    NormalizedName = Column(String(256), unique=True)
    ConcurrencyStamp = Column(Text)

    AspNetUsers = relationship('AspNetUser', secondary='AspNetUserRoles')


class AspNetUser(Base):
    __tablename__ = 'AspNetUsers'

    Id = Column(Text, primary_key=True)
    UserName = Column(String(256))
    NormalizedUserName = Column(String(256), unique=True)
    Email = Column(String(256))
    NormalizedEmail = Column(String(256), index=True)
    EmailConfirmed = Column(Boolean, nullable=False)
    PasswordHash = Column(Text)
    SecurityStamp = Column(Text)
    ConcurrencyStamp = Column(Text)
    PhoneNumber = Column(Text)
    PhoneNumberConfirmed = Column(Boolean, nullable=False)
    TwoFactorEnabled = Column(Boolean, nullable=False)
    LockoutEnd = Column(DateTime(True))
    LockoutEnabled = Column(Boolean, nullable=False)
    AccessFailedCount = Column(Integer, nullable=False)


class Audit(Base):
    __tablename__ = 'Audit'

    Id = Column(Integer, primary_key=True, server_default=text("nextval('\"Audit_Id_seq\"'::regclass)"))
    TableName = Column(Text, nullable=False)
    DateTime = Column(Time, nullable=False)
    KeyValues = Column(Text, nullable=False)
    OldValues = Column(Text, nullable=False)
    NewValues = Column(Text, nullable=False)


class EFMigrationsHistory(Base):
    __tablename__ = '__EFMigrationsHistory'

    MigrationId = Column(String(150), primary_key=True)
    ProductVersion = Column(String(32), nullable=False)


class AppAccountUser(Base):
    __tablename__ = 'app_account_user'

    id = Column(UUID, primary_key=True)
    account_id = Column(Text, nullable=False)
    user_id = Column(Text, nullable=False)
    active = Column(Integer, nullable=False)


class AppAccount(Base):
    __tablename__ = 'app_accounts'

    id = Column(String(36), primary_key=True)
    name = Column(String(45), server_default=text("'NULL'::character varying"))
    code = Column(String(5), server_default=text("'NULL'::character varying"))
    account_type = Column(Integer, index=True)
    created_at = Column(DateTime)
    created_by = Column(String(128), server_default=text("'NULL'::character varying"))


class AppCountry(Base):
    __tablename__ = 'app_country'

    id = Column(Integer, primary_key=True, server_default=text("nextval('app_countries_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    code = Column(Text)
    latitude = Column(Text)
    longitude = Column(Text)


class AppForm(Base):
    __tablename__ = 'app_form'

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    module_id = Column(Text, nullable=False)
    enabled = Column(Boolean, nullable=False)


class AppModule(Base):
    __tablename__ = 'app_module'

    id = Column(String(36), primary_key=True)
    name = Column(String(100), server_default=text("'NULL'::character varying"))
    enabled = Column(String(1), server_default=text("'N'::character varying"))
    description = Column(Text)


class AppNotification(Base):
    __tablename__ = 'app_notification'

    id = Column(Integer, primary_key=True, server_default=text("nextval('app_notification_id_seq'::regclass)"))
    type_id = Column(Integer, nullable=False)
    notification = Column(Text, nullable=False)
    account_id = Column(Text, nullable=False)
    user_id = Column(Text, nullable=False)
    viewed = Column(Integer, nullable=False)
    created_by = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)


class AppNotificationType(Base):
    __tablename__ = 'app_notification_type'

    id = Column(Integer, primary_key=True, server_default=text("nextval('app_notification_type_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    template = Column(Text)


class AppSetting(Base):
    __tablename__ = 'app_settings'

    id = Column(Integer, primary_key=True, server_default=text("nextval('app_settings_id_seq'::regclass)"))
    key = Column(String(150), nullable=False)
    value = Column(String(500), nullable=False)


class AppUserService(Base):
    __tablename__ = 'app_user_service'

    id = Column(Integer, primary_key=True, server_default=text("nextval('app_user_service_id_seq'::regclass)"))
    user_id = Column(Text, nullable=False)
    service_id = Column(Text, nullable=False)
    role_id = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(Text)
    token = Column(Text, nullable=False)


class AppVersion(Base):
    __tablename__ = 'app_version'

    id = Column(Integer, primary_key=True, server_default=text("nextval('app_version_id_seq'::regclass)"))
    v_no = Column(Text, nullable=False)
    v_date = Column(DateTime, nullable=False)


class CrmActiveContact(Base):
    __tablename__ = 'crm_active_contacts'

    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('crm_active_contacts_id_seq'::regclass)"))
    contact_id = Column(CHAR(36), primary_key=True, nullable=False)
    user_id = Column(String(128), nullable=False)
    time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    active = Column(Integer, nullable=False, server_default=text("0"))


class CrmAuditSetting(Base):
    __tablename__ = 'crm_audit_settings'

    id = Column(Integer, primary_key=True, server_default=text("nextval('crm_audit_settings_id_seq'::regclass)"))
    action = Column(String(100), server_default=text("'NULL'::character varying"))
    description_template = Column(String(500), server_default=text("'NULL'::character varying"))


class CrmAuditTrail(Base):
    __tablename__ = 'crm_audit_trail'

    id = Column(CHAR(36), primary_key=True)
    audit_time = Column(DateTime)
    action = Column(String(100), server_default=text("'NULL'::character varying"))
    user = Column(Integer)
    section = Column(String(100), server_default=text("'NULL'::character varying"))
    action_description = Column(String(500), server_default=text("'NULL'::character varying"))
    service_id = Column(String(45), server_default=text("'NULL'::character varying"))
    created_at = Column(DateTime)


class CrmCaseCategory(Base):
    __tablename__ = 'crm_case_category'

    id = Column(Integer, primary_key=True, server_default=text("nextval('crm_case_category_id_seq'::regclass)"))
    service_id = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    value = Column(Text, nullable=False)
    deleted = Column(Integer, nullable=False)


class CrmCaseConversation(Base):
    __tablename__ = 'crm_case_conversations'

    id = Column(CHAR(36), primary_key=True)
    case_id = Column(CHAR(36), server_default=text("'NULL'::bpchar"))
    conversation_id = Column(CHAR(36), server_default=text("'NULL'::bpchar"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class CrmCaseNote(Base):
    __tablename__ = 'crm_case_notes'

    id = Column(CHAR(36), primary_key=True)
    note = Column(Text)
    case_id = Column(CHAR(36), server_default=text("'NULL'::bpchar"))
    user_id = Column(String(128), server_default=text("'NULL'::character varying"))
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime)


class CrmContact(Base):
    __tablename__ = 'crm_contacts'

    service_id = Column(String(36), nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime)
    contact_object = Column(JSON)
    last_name = Column(Text)
    first_name = Column(Text)
    phone_number = Column(Text)
    created_by = Column(Text)
    code = Column(Text)
    updated_by = Column(Text)
    deleted = Column(Integer)
    id = Column(UUID, primary_key=True)
    twitter = Column(Text)



class CrmConversationSource(Base):
    __tablename__ = 'crm_conversation_source'

    id = Column(Integer, primary_key=True, server_default=text("nextval('crm_conversation_source_id_seq'::regclass)"))
    name = Column(Text)
    icon = Column(Text)


class CrmLookup(Base):
    __tablename__ = 'crm_lookup'

    lookup_name = Column(String(20), nullable=False)
    lookup_value = Column(String(500), nullable=False)
    value_order = Column(Integer)
    parent_id = Column(Integer)
    service_id = Column(Text)
    id = Column(Integer, primary_key=True)
    deleted = Column(Integer, server_default=text("0"))


class CrmNotificationType(Base):
    __tablename__ = 'crm_notification_type'

    id = Column(Integer, primary_key=True)
    notification = Column(String(45), server_default=text("'NULL'::character varying"))
    message = Column(String(500), server_default=text("'NULL'::character varying"))


class CrmNotification(Base):
    __tablename__ = 'crm_notifications'

    id = Column(CHAR(36), primary_key=True)
    user_id = Column(String(128), server_default=text("'NULL'::character varying"))
    link = Column(String(150), server_default=text("'NULL'::character varying"))
    notification_type = Column(Integer)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    viewed = Column(Integer)
    assigned_by = Column(String(128), server_default=text("'NULL'::character varying"))
    content = Column(Text)


class CrmSmsToken(Base):
    __tablename__ = 'crm_sms_token'

    id = Column(Integer, primary_key=True, server_default=text("nextval('crm_sms_token_id_seq'::regclass)"))
    service_id = Column(String(36), nullable=False, index=True)
    token = Column(String(16), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(36), nullable=False)


class CrmUserAccount(Base):
    __tablename__ = 'crm_user_account'

    id = Column(Integer, primary_key=True, server_default=text("nextval('crm_user_account_id_seq'::regclass)"))
    user_id = Column(String(128), server_default=text("'NULL'::character varying"))
    account_id = Column(String(36), server_default=text("'NULL'::character varying"))
    is_active = Column(SmallInteger)


class CrmUserService(Base):
    __tablename__ = 'crm_user_service'

    id = Column(Integer, primary_key=True, server_default=text("nextval('crm_user_service_id_seq'::regclass)"))
    user_id = Column(String(128), nullable=False, index=True)
    service_id = Column(String(36), nullable=False, index=True)
    is_active = Column(Integer, nullable=False, server_default=text("0"))


class KnmKnowledgeCategory(Base):
    __tablename__ = 'knm_knowledge_category'

    id = Column(UUID, primary_key=True)
    service_id = Column(String(36), nullable=False)
    category = Column(String(150), nullable=False)


t_test = Table(
    'test', metadata,
    Column('cases', JSON)
)


class AspNetRoleClaim(Base):
    __tablename__ = 'AspNetRoleClaims'

    Id = Column(Integer, primary_key=True, server_default=text("nextval('\"AspNetRoleClaims_Id_seq\"'::regclass)"))
    RoleId = Column(ForeignKey('AspNetRoles.Id', ondelete='CASCADE'), nullable=False, index=True)
    ClaimType = Column(Text)
    ClaimValue = Column(Text)

    AspNetRole = relationship('AspNetRole')


class AspNetUserClaim(Base):
    __tablename__ = 'AspNetUserClaims'

    Id = Column(Integer, primary_key=True, server_default=text("nextval('\"AspNetUserClaims_Id_seq\"'::regclass)"))
    UserId = Column(ForeignKey('AspNetUsers.Id', ondelete='CASCADE'), nullable=False, index=True)
    ClaimType = Column(Text)
    ClaimValue = Column(Text)

    AspNetUser = relationship('AspNetUser')


class AspNetUserLogin(Base):
    __tablename__ = 'AspNetUserLogins'

    LoginProvider = Column(String(128), primary_key=True, nullable=False)
    ProviderKey = Column(String(128), primary_key=True, nullable=False)
    ProviderDisplayName = Column(Text)
    UserId = Column(ForeignKey('AspNetUsers.Id', ondelete='CASCADE'), nullable=False, index=True)

    AspNetUser = relationship('AspNetUser')


t_AspNetUserRoles = Table(
    'AspNetUserRoles', metadata,
    Column('UserId', ForeignKey('AspNetUsers.Id', ondelete='CASCADE'), primary_key=True, nullable=False),
    Column('RoleId', ForeignKey('AspNetRoles.Id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


class AspNetUserToken(Base):
    __tablename__ = 'AspNetUserTokens'

    UserId = Column(ForeignKey('AspNetUsers.Id', ondelete='CASCADE'), primary_key=True, nullable=False)
    LoginProvider = Column(String(128), primary_key=True, nullable=False)
    Name = Column(String(128), primary_key=True, nullable=False)
    Value = Column(Text)

    AspNetUser = relationship('AspNetUser')


# class AppMessaging(Base):
#     __tablename__ = 'app_messaging'
#
#     id = Column(Integer, primary_key=True, server_default=text("nextval('app_messaging_id_seq'::regclass)"))
#     _from = Column('from', ForeignKey('AspNetUsers.Id'), nullable=False)
#     to = Column(ForeignKey('AspNetUsers.Id'), nullable=False)
#     message = Column(Text, nullable=False)
#     created_at = Column(DateTime, nullable=False)
#     viewed = Column(Integer, nullable=False)
#     account_id = Column(Text, nullable=False)
#
#     AspNetUser = relationship('AspNetUser', primaryjoin='AppMessaging.from == AspNetUser.Id')
#     AspNetUser1 = relationship('AspNetUser', primaryjoin='AppMessaging.to == AspNetUser.Id')


class AppService(Base):
    __tablename__ = 'app_services'

    id = Column(String(36), primary_key=True)
    name = Column(String(150), server_default=text("'NULL'::character varying"))
    code = Column(String(5), server_default=text("'NULL'::character varying"))
    tw_consumer_key = Column(String(45), server_default=text("'NULL'::character varying"))
    tw_consumer_secret = Column(String(45), server_default=text("'NULL'::character varying"))
    tw_access_token = Column(String(45), server_default=text("'NULL'::character varying"))
    tw_access_token_secret = Column(String(45), server_default=text("'NULL'::character varying"))
    tw_status = Column(SmallInteger)
    tw_screen_name = Column(String(45), server_default=text("'NULL'::character varying"))
    sms_token = Column(String(45), server_default=text("'NULL'::character varying"))
    account_id = Column(ForeignKey('app_accounts.id'))
    address = Column(Text)
    phone = Column(Text)
    email = Column(Text)
    ticket_prefix = Column(Text)
    created_at = Column(DateTime)
    created_by = Column(Text)
    twitter_id = Column(Text)

    account = relationship('AppAccount')


class AppUserProfile(Base):
    __tablename__ = 'app_user_profile'

    id = Column(Integer, primary_key=True, server_default=text("nextval('crm_user_profiles_id_seq'::regclass)"))
    user_id = Column(ForeignKey('AspNetUsers.Id'), nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    gender = Column(Integer)
    country = Column(Integer)
    state = Column(Integer)
    city = Column(Text)
    address = Column(Text)
    designation = Column(Text)
    status = Column(Text)

    user = relationship('AspNetUser')


class CrmCase(Base):
    __tablename__ = 'crm_cases'

    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime)
    case_notes = Column(Text)
    ticket_id = Column(String(45), server_default=text("'NULL'::character varying"))
    assigned_to_user = Column(String(128), server_default=text("'NULL'::character varying"))
    service_id = Column(String(45), server_default=text("'NULL'::character varying"))
    viewed = Column(Integer)
    case_object = Column(JSON)
    id = Column(UUID, primary_key=True)
    created_by = Column(Text)
    updated_by = Column(Text)
    deleted = Column(Integer)
    contact_id = Column(ForeignKey('crm_contacts.id'))
    category_id = Column(Text)
    status = Column(Text)

    contact = relationship('CrmContact')


class CrmConversation(Base):
    __tablename__ = 'crm_conversations'

    conversation = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False)
    created_by = Column(Text)
    service_id = Column(Text, nullable=False)
    source_id = Column(ForeignKey('crm_conversation_source.id'), nullable=False)
    viewed = Column(Integer, nullable=False)
    type_id = Column(Integer, nullable=False)
    id = Column(UUID, primary_key=True)
    contact_id = Column(ForeignKey('crm_contacts.id'), nullable=False)
    direction = Column(Text, nullable=False)

    contact = relationship('CrmContact')
    source = relationship('CrmConversationSource')


class AppModuleTemplate(Base):
    __tablename__ = 'app_module_templates'

    id = Column(String(36), primary_key=True)
    module_template_object = Column(Text)
    module_id = Column(ForeignKey('app_module.id'), server_default=text("'NULL'::character varying"))
    service_id = Column(ForeignKey('app_services.id'))
    form_id = Column(ForeignKey('app_form.id'))
    form_location_id = Column(Integer)

    form = relationship('AppForm')
    module = relationship('AppModule')
    service = relationship('AppService')


class AppServiceModule(Base):
    __tablename__ = 'app_service_module'

    id = Column(Text, primary_key=True)
    service_id = Column(ForeignKey('app_services.id'), nullable=False)
    module_id = Column(ForeignKey('app_module.id'), nullable=False)
    active = Column(Integer, nullable=False)

    module = relationship('AppModule')
    service = relationship('AppService')


class AppUserActiveService(Base):
    __tablename__ = 'app_user_active_service'

    id = Column(Integer, primary_key=True, server_default=text("nextval('app_user_active_service_id_seq'::regclass)"))
    user_id = Column(Text, nullable=False)
    service_id = Column(ForeignKey('app_services.id'))

    service = relationship('AppService')


class CrmCaseDuration(Base):
    __tablename__ = 'crm_case_duration'

    open_time = Column(TIMESTAMP(precision=4), nullable=False)
    closed_time = Column(DateTime, nullable=False)
    created_by = Column(Text, nullable=False)
    case_id = Column(ForeignKey('crm_cases.id'), nullable=False)
    id = Column(Integer, primary_key=True, server_default=text("nextval('crm_case_duration_id_seq'::regclass)"))
    service_id = Column(Text)

    case = relationship('CrmCase')


class KnmKnowledge(Base):
    __tablename__ = 'knm_knowledge'

    id = Column(UUID, primary_key=True)
    title = Column(Text, nullable=False)
    service_id = Column(ForeignKey('app_services.id'), nullable=False)
    category_id = Column(ForeignKey('knm_knowledge_category.id'), nullable=False)
    value = Column(Text, nullable=False)
    created_by = Column(String(36), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_by = Column(String(36))
    updated_at = Column(DateTime)

    category = relationship('KnmKnowledgeCategory')
    service = relationship('AppService')
