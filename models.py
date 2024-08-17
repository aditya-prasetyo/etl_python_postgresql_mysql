from sqlalchemy import MetaData
from sqlalchemy import (Table,
                        Column,
                        BigInteger,
                        Integer,
                        VARCHAR,
                        JSON,
                        Text,
                        TIMESTAMP,
                        Index,
                        Numeric,
                        Float,
                        DateTime,
                        UniqueConstraint,
                        Boolean,
                        VARCHAR,
                        String,
                        func,
                        text,
                        desc
                        )
from datetime import datetime

metadata_obj = MetaData()

ActivityHistory = Table(
    "ActivityHistory",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default='{}'),
    Column("modifiedBy", JSON, default='{}'),
    Column("version", Integer, default=1),
    Column("id", Integer,
           primary_key=True),
    Column("adminId", Integer),
    Column("actionTypeId", Integer),
    Column("menu", VARCHAR(150)),
    Column("description", Text),

)

Admin = Table(
    "Admin",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default='{}'),
    Column("modifiedBy", JSON, default='{}'),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column('xid', VARCHAR(16)),
    Column('fullName', VARCHAR(255)),
    Column('username', VARCHAR(100), unique=True),
    Column('roleId', BigInteger),
    Column('statusId', Integer),
    Column('roleXid', VARCHAR(6)),
)


AdminAuth = Table(
    "AdminAuth",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default='{}'),
    Column("modifiedBy", JSON, default='{}'),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column('adminId', BigInteger),
    Column('clientId', VARCHAR(100)),
    Column('clientSecret', JSON),
    Column('statusId', Integer),
)

Ads = Table(
    "Ads",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("modifiedBy", JSON, default='{}'),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default='{}'),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column('xid', VARCHAR(16)),
    Column('name', VARCHAR(255)),
    Column('statusId', Integer),
    Column('periodStart', TIMESTAMP),
    Column('periodEnd', TIMESTAMP),
    Column('content', JSON),
)


AdsStation = Table(
    "AdsStation",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("modifiedBy", JSON, default='{}'),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column('stationId', BigInteger),
    Column('stationXid', VARCHAR(10)),
    Column('adsId', BigInteger),
    Column('adsXid', VARCHAR(16)),
)


ApplicationLog = Table(
    "ApplicationLog",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("modifiedBy", JSON, default='{}'),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default='{}'),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column('xid', VARCHAR(16)),
    Column('apkFile', VARCHAR(255)),
    Column('description', Text),
    Column('versionApp', VARCHAR(255)),
    Column('statusId', Integer),
)


AuthProvider = Table(
    "AuthProvider",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default='{}'),
    Column("modifiedBy", JSON, default='{}'),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column('name', VARCHAR(255)),
)


AuthSession = Table(
    "AuthSession",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default='{}'),
    Column("modifiedBy", JSON, default='{}'),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column('xid', VARCHAR(16)),
    Column('subjectTypeId', BigInteger),
    Column('subjectId', VARCHAR(255)),
    Column('authProviderId', Integer),
    Column('devicePlatformId', Integer),
    Column('deviceId', VARCHAR(255)),
    Column('device', JSON, default='{}'),
    Column('notificationChannelId', Integer),
    Column('notificationToken', VARCHAR(255), nullable=True),
    Column('expiredAt', TIMESTAMP),
    Column('statusId', Integer),
)


Banner = Table(
    "Banner",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default='{}'),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column("xid", VARCHAR(6)),
    Column("tenantId", Integer),
    Column("description", Text),
    Column("url", Text),
    Column("viewTypeId", BigInteger),
    Column("bannerTypeId", Integer),
    Column("sort", Integer, default=1),
    Column("image", VARCHAR(255)),
    Column("startDate", TIMESTAMP),
    Column("endDate", TIMESTAMP),
    Column("title", JSON, default=None),
)


BannerType = Table(
    "BannerType",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", Integer, primary_key=True),
    Column("name", VARCHAR(255)),
)


BannerViewType = Table(
    "BannerViewType",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default=None),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column("name", VARCHAR(32)),
)


CardProvider = Table(
    "CardProvider",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default=None),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column("name", VARCHAR(64)),
    Column("logo", VARCHAR(64)),
    Column("statusId", Integer),
    # You can add more columns or constraints as needed
)


ClientAuth = Table(
    "ClientAuth",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default=None),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column("name", VARCHAR(255)),
    Column("clientId", VARCHAR(8)),
    Column("clientTypeId", BigInteger),
    Column("options", JSON),
    Column("statusId", Integer),
)


ControlStatus = Table(
    "ControlStatus",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default=None),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", Integer, primary_key=True),
    Column("name", VARCHAR(255)),
)


DevicePlatform = Table(
    "DevicePlatform",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default=None),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", Integer, primary_key=True),
    Column("name", VARCHAR(255)),
)


DisplayGroup = Table(
    "DisplayGroup",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default=None),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column("name", VARCHAR(50)),
)


Entertainment = Table(
    "Entertainment",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default=None),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column("xid", VARCHAR(6)),
    Column("partnerId", BigInteger),
    Column("partnerXid", VARCHAR(4)),
    Column("entertainmentTypeId", BigInteger),
    Column("title", VARCHAR(255)),
    Column("content", JSON),
    Column("displayGroupId", BigInteger),
    Column("sort", Integer),
    Column("statusId", Integer),
)


EntertainmentPartner = Table(
    "EntertainmentPartner",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default=None),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column("xid", VARCHAR(4)),
    Column("entertainmentTypeId", BigInteger),
    Column("name", VARCHAR(50)),
    Column("logo", VARCHAR(128), default=""),
    Column("statusId", Integer),
)


EntertainmentType = Table(
    "EntertainmentType",
    metadata_obj,
    Column("createdAt", TIMESTAMP),
    Column("updatedAt", TIMESTAMP),
    Column("metadata", JSON, default=None),
    Column("modifiedBy", JSON),
    Column("version", Integer, default=1),
    Column("id", BigInteger,
           primary_key=True),
    Column("name", VARCHAR(10)),
)


Event = Table(
    'Event',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('tenantId', Integer),
    Column('tenantXid', VARCHAR(4)),
    Column('viewTypeId', Integer),
    Column('statusId', Integer),
    Column('name', VARCHAR(200)),
    Column('content', JSON),
    Column('sort', Integer, default=1),
    Column('startedAt', TIMESTAMP),
    Column('endedAt', TIMESTAMP),
    Column('liveStartedAt', TIMESTAMP),
    Column('liveEndedAt', TIMESTAMP),
)


Facility = Table(
    'Facility',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(4)),
    Column('name', VARCHAR(255)),
    Column('nameEn', VARCHAR(255)),
    Column('icon', VARCHAR(255)),
    Column('statusId', Integer),
)


Faq = Table(
    'Faq',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('categoryId', Integer),
    Column('categoryXid', VARCHAR(4)),
    Column('statusId', Integer),
    Column('question', Text),  # Adjust the data type as needed
    Column('answer', Text),    # Adjust the data type as needed
    # Add any additional columns or constraints here
    # ...
)


FaqCategory = Table(
    'FaqCategory',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(4)),
    Column('name', VARCHAR(255)),
    # Adjust the data type as needed
    Column('description', Text),
    Column('statusId', Integer, default=1),
    # Add any additional columns or constraints here
    # ...
)


InvoiceStatus = Table(
    'InvoiceStatus',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('name', VARCHAR(32)),
    # Add any additional columns or constraints here
    # ...
)


KeyValueStore = Table(
    'KeyValueStore',
    metadata_obj,
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('key', VARCHAR(64)),
    Column('value', JSON),
    # Add any additional columns or constraints here
    # ...
)


Lifestyle = Table(
    'Lifestyle',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(4)),
    Column('categoryId', BigInteger),
    Column('name', VARCHAR(255)),
    Column('code', VARCHAR(64)),
    Column('tagLineId', VARCHAR(255)),
    Column('tagLineEn', VARCHAR(255)),
    Column('sort', Integer),
    Column('logo', VARCHAR(128)),
    Column('statusId', Integer),
    Column('options', JSON),
    # Add any additional columns or constraints here
    # ...
)


LifestyleCategory = Table(
    'LifestyleCategory',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('nameId', VARCHAR(128)),
    Column('nameEn', VARCHAR(128)),
    Column('sort', Integer),
    # Add any additional columns or constraints here
    # ...
)

MigrationLog = Table(
    'MigrationLog',
    metadata_obj,
    Column('id', BigInteger,primary_key = True),
    Column('createdAt', TIMESTAMP),
    Column('table', VARCHAR(100)),
    Column('flag', VARCHAR(100)),
    Column('process', VARCHAR(100)),
    Column('description', Text),
    Index('idx_migrationlog_createdAt_table', 'createdAt', 'table')
    # Add any additional columns or constraints here
    # ...
)

MyCard = Table(
    'MyCard',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('userId', BigInteger,  nullable=False),
    Column('providerId', BigInteger),
    Column('cardNumber', VARCHAR(32)),
    # Indexes
    Index('IDX_MyCard__providerId', 'providerId'),
    Index('IDX_MyCard__userId', 'userId'),
    # Add any additional columns or constraints here
    # ...
)


Notification = Table(
    'Notification',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(8)),
    Column('content', JSON),
    Column('statusId', Integer),
    Column('broadcastAt', TIMESTAMP),
    Column('title', VARCHAR(200), default=''),
    Column('scheduledAt', TIMESTAMP),
    Column('flag', Integer),
    # Add any additional columns or constraints here
    # ...
)


NotificationChannel = Table(
    'NotificationChannel',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('name', VARCHAR(255)),
    # Add any additional columns or constraints here
    # ...
)


Otp = Table(
    'Otp',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('sessionId', BigInteger),
    Column('otpNo', Integer),
    Column('signature', VARCHAR(255)),
    # Add any additional columns or constraints here
    # ...
)


OtpSession = Table(
    'OtpSession',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('requestId', VARCHAR(64)),
    Column('purpose', Integer),
    Column('phone', VARCHAR(255)),
    Column('rule', JSON),
    Column('otpCount', Integer),
    Column('failAttemptCount', Integer),
    Column('nextResendAt', TIMESTAMP),
    Column('expiredAt', TIMESTAMP),
    # Add any additional columns or constraints here
    # ...
)


PaymentMethod = Table(
    'PaymentMethod',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('name', VARCHAR(32)),
    Column('statusId', Integer),
    Column('logo', VARCHAR(255), default=None),
    Column('transactionTypeId', BigInteger),
    Column('sort', Integer),
    Column('listed', Integer, default=1),
    # Add any additional columns or constraints here
    # ...
)

PosDevice = Table(
    'PosDevice',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('userId', BigInteger, default=None),
    Column('deviceId', VARCHAR(128)),
    Column('name', VARCHAR(128)),
    Column('statusId', Integer),
    Column('locationLat', Float, default=None),
    Column('locationLng', Float, default=None),
    Column('locationDescription', Text, default=None),
    Column('boundAt', TIMESTAMP, default=None),
    Column('boundIp', VARCHAR(155), default=None),
    Column('lastConnectedAt', TIMESTAMP, default=None),
    Column('lastConnectedIp', VARCHAR(255), default=None),
    # Add any additional columns or constraints here
    # ...
)

PosUser = Table(
    'PosUser',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('extId', VARCHAR(128)),
    Column('fullName', VARCHAR(128)),
    Column('statusId', Integer),
    Column('clientId', VARCHAR(100)),
    Column('clientSecret', JSON),
    UniqueConstraint('extId', name='IDX_PosUser__extId'),
    UniqueConstraint('clientId', name='IDX_PosUser__username'),
    Index('IDX_PosUser__xid', 'xid'),
    # Add any additional columns or constraints here
    # ...
)


Privilege = Table(
    'Privilege',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(20)),
    Column('name', VARCHAR(255)),
    Column('exposed', Boolean, default=False),
    UniqueConstraint('xid', name='privilege_xid_unique'),
    # Add any additional columns or constraints here
    # ...
)


Report = Table(
    'Report',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(4)),
    Column('categoryId', Integer, default=None),
    Column('categoryXid', VARCHAR(4), default=None),
    Column('userId', BigInteger),
    Column('userXid', VARCHAR(16)),
    Column('userSnapshot', JSON),
    Column('content', JSON),
    Column('name', VARCHAR(255), default=''),
    Column('stationId', Integer, default=1),
    Column('stationXid', VARCHAR(10), default=''),
    Column('facilityId', Integer, default=1),
    Column('facilityXid', VARCHAR(4), default=''),
    Column('categorySnapshot', JSON, default={"xid": "", "version": 1, "name": "", "description": "", "status": {
           "id": 0, "name": "Unknown"}, "createdAt": 0, "updatedAt": 0, "modifiedBy": {"id": "", "role": "", "fullName": ""}}),
    # Add any additional columns or constraints here
    # ...
)


ReportCategory = Table(
    'ReportCategory',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(4)),
    Column('name', VARCHAR(255)),
    Column('description', Text),
    Column('statusId', Integer),
    # Add any additional columns or constraints here
    # ...
)


RewardClaimStatus = Table(
    'RewardClaimStatus',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer),
    Column('name', VARCHAR(255)),
    # Add any additional columns or constraints here
    # ...
)


RewardProgram = Table(
    'RewardProgram',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer),
    Column('xid', VARCHAR(16)),
    Column('scenarioId', BigInteger),
    Column('name', VARCHAR(255)),
    Column('orgUnitId', VARCHAR(8)),
    Column('orgUnit', JSON),
    Column('statusId', Integer),
    Column('periodStart', TIMESTAMP),
    Column('periodEnd', TIMESTAMP),
    Column('quota', Integer),
    Column('userQuota', Integer),
    Column('claimRules', JSON),
    Column('rewardRules', JSON),
    Column('priority', Integer),
    Column('revision', Integer),
    Column('content', JSON),
    Column('listed', Boolean),
    Column('quotaClaimed', Integer),
    Column('quotaAvailable', Integer),
    Index('IDX_RewardProgram_1', 'xid'),
    Index('IDX_RewardProgram_2', 'scenarioId', 'statusId',
          'periodStart', 'periodEnd', 'listed', text('priority desc')),
    # Add any additional columns or constraints here
    # ...
)


RewardProgramPaymentMethod = Table(
    'RewardProgramPaymentMethod',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer),
    Column('programId', BigInteger),
    Column('paymentMethodId', BigInteger, default=None),
    Index('IDX_RewardProgramPaymentMethod_1', 'paymentMethodId', 'programId'),
    # Add any additional columns or constraints here
    # ...
)


RewardProgramScenario = Table(
    'RewardProgramScenario',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer),
    Column('name', VARCHAR(255)),
    # Add any additional columns or constraints here
    # ...
)


RewardProgramStation = Table(
    'RewardProgramStation',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer),
    Column('programId', BigInteger),
    Column('stationId', BigInteger, default=None),
    Column('originStation', Boolean),
    Column('destinationStation', Boolean),
    Index('IDX_RewardProgramStation_1', 'programId',
          'stationId', 'originStation', 'destinationStation'),
    # Add any additional columns or constraints here
    # ...
)


Role = Table(
    'Role',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('name', VARCHAR(255)),
    Column('roleTypeId', Integer),
    Column('statusId', Integer, default=1),
    Column('description', Text, default=''),
    # Add any additional columns or constraints here
    # ...
)


RolePaymentMethod = Table(
    'RolePaymentMethod',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP, server_default=func.now()),
    Column('updatedAt', TIMESTAMP, server_default=func.now()),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('roleId', BigInteger),
    Column('paymentMethodId', BigInteger),
    Column('statusId', Integer),
    Column('sort', Integer, default=99),
    Column('notes', JSON),
    UniqueConstraint('roleId', 'paymentMethodId',
                     name='IDX_RolePaymentMethod_uniqueByPlatform'),
    Index('IDX_RolePaymentMethod_sortByPlatform',
          'roleId', 'paymentMethodId', 'sort'),
    # Add any additional columns or constraints here
    # ...
)


RolePrivilege = Table(
    'RolePrivilege',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('roleId', BigInteger),
    Column('privilegeId', BigInteger),
    # Add any additional columns or constraints here
    # ...
)


RoleType = Table(
    'RoleType',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('name', VARCHAR(255)),
    # Add any additional columns or constraints here
    # ...
)


RouteType = Table(
    'RouteType',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('name', VARCHAR(255)),
    # Add any additional columns or constraints here
    # ...
)


SessionRegister = Table(
    'SessionRegister',
    metadata_obj,
    Column('id', VARCHAR(255), primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('fullName', VARCHAR(255)),
    Column('phone', VARCHAR(16)),
    Column('email', VARCHAR(255)),
    Column('age', VARCHAR(32), default=None),
    Column('statusId', Integer),
    Column('notificationChannelId', Integer, default=None),
    Column('notificationToken', VARCHAR(255), default=None),
    Column('clientSecret', JSON, default=None),
    Column('oauth', JSON, default=None),
    # Add any additional columns or constraints here
    # ...
)


Station = Table(
    'Station',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(10)),
    Column('code', VARCHAR(255)),
    Column('name', VARCHAR(255)),
    Column('alias', VARCHAR(255)),
    Column('sort', Integer),
    Column('pointLat', Float),
    Column('pointLong', Float),
    Column('statusId', Integer, default=None),
    Column('content', JSON),
    Column('lpRefId', Integer),
    Index('idx_Station_1', 'xid', 'statusId'),
    # Add any additional columns or constraints here
    # ...
)


StationExitGate = Table(
    'StationExitGate',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('stationId', BigInteger),
    Column('stationXid', VARCHAR(10)),
    Column('name', VARCHAR(50)),
    Column('description', Text),
    Column('descriptionHtml', Text),
    Index('IDX_StationExitGate__stationXid', 'stationXid'),
    # Add any additional columns or constraints here
    # ...
)


StationFacility = Table(
    'StationFacility',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('stationId', BigInteger),
    Column('stationXid', VARCHAR(10)),
    Column('facilityId', BigInteger),
    Column('facilityXid', VARCHAR(4)),
    Column('name', VARCHAR(255)),
    Column('description', Text),
    Column('statusId', Integer),
    # Add any additional columns or constraints here
    # ...
)


StationSchedule = Table(
    'StationSchedule',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('trainId', VARCHAR(255)),
    Column('routeTypeId', Integer),
    Column('startStationId', BigInteger),
    Column('startStationName', VARCHAR(255)),
    Column('endStationId', BigInteger),
    Column('endStationName', VARCHAR(255)),
    Column('startStationSnapshot', JSON),
    Column('endStationSnapshot', JSON),
    Column('arrivalTime', TIMESTAMP),
    Column('departureTime', TIMESTAMP),
    # Add any additional columns or constraints here
    # ...
)


StationTicketPrice = Table(
    'StationTicketPrice',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('originStationId', BigInteger),
    Column('originStationName', VARCHAR(255)),
    Column('destinationStationId', BigInteger),
    Column('destinationStationName', VARCHAR(255)),
    Column('amount', Numeric(20, 2)),
    # Add any additional columns or constraints here
    # ...
)

SurroundingArea = Table(
    'SurroundingArea',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('categoryId', Integer),
    Column('categoryXid', VARCHAR(50)),
    Column('name', VARCHAR(255)),
    Column('address', Text),
    Column('content', JSON),
    Column('statusId', Integer),
    # Add any additional columns or constraints here
    # ...
)


SurroundingAreaCategory = Table(
    'SurroundingAreaCategory',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(4)),
    Column('name', VARCHAR(50)),
    Column('statusId', Integer),
    Column('code', VARCHAR(50), default=''),
    # Add any additional columns or constraints here
    # ...
)


Tenant = Table(
    'Tenant',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(4)),
    Column('name', VARCHAR(255)),
    Column('description', Text),
    Column('logo', VARCHAR(255)),
    Column('categoryId', Integer),
    Column('categoryXid', VARCHAR(4)),
    Column('statusId', Integer),
    # Add any additional columns or constraints here
    # ...
)


TenantCategory = Table(
    'TenantCategory',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(4)),
    Column('name', VARCHAR(255)),
    Column('description', Text),
    Column('statusId', Integer),
    # Add any additional columns or constraints here
    # ...
)


TenantStation = Table(
    'TenantStation',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('tenantId', BigInteger),
    Column('tenantXid', VARCHAR(4)),
    Column('stationId', BigInteger),
    Column('stationXid', VARCHAR(10)),
    Column('kioskNumber', VARCHAR(36)),
    Column('description', Text),
    Column('statusId', Integer),
    # Add any additional columns or constraints here
    # ...
)

TermCondition = Table(
    'TermCondition',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(4)),
    Column('categoryName', VARCHAR(255)),
    Column('description', Text),
    # Add any additional columns or constraints here
    # ...
)


Theme = Table(
    'Theme',
    metadata_obj,
    Column('id', BigInteger),
    Column('createdAt', DateTime),
    Column('updatedAt', DateTime),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', BigInteger),
    Column('xid', VARCHAR(100)),
    Column('name', VARCHAR(255)),
    Column('statusId', BigInteger),
    Column('periodStart', DateTime),
    Column('periodEnd', DateTime),
    Column('hexColor', VARCHAR(255)),
    # Add any additional columns or constraints here
    # ...
)


TicketDeliveryMethod = Table(
    'TicketDeliveryMethod',
    metadata_obj,
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer),
    Column('id',Integer,primary_key = True),
    Column('name', VARCHAR(255)),
    Column('listed', Boolean)
)

Ticket = Table(
    'Ticket',
    metadata_obj,
    Column('id', VARCHAR(255)),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('invoiceId', VARCHAR(255)),
    Column('seqNumber', Integer),
    Column('ticketNumber', VARCHAR(36),primary_key=True),
    Column('userId', Integer),
    Column('trip', JSON),
    Column('originStationId', Integer),
    Column('destinationStationId', Integer),
    Column('statusId', BigInteger),
    Column('expiredAt', TIMESTAMP),
    Column('qrRef', VARCHAR(36), default=None),
    Column('tapInQrCode', VARCHAR(36), default=None),
    Column('tapOutQrCode', VARCHAR(36), default=None),
    Column('tapInAt', TIMESTAMP),
    Column('tapOutAt', TIMESTAMP),
    Column('ticketRefId', VARCHAR(255), default=None),
    Column('flagId', BigInteger, default=0),
    Column('log', JSON),
    Column('directionId', BigInteger, default=1),
    # Column('id_no', BigInteger),
    # Add any additional columns or constraints here
    # ...
)


TicketFlag = Table(
    'TicketFlag',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('name', VARCHAR(32)),
    # Add any additional columns or constraints here
    # ...
)


TicketInvoice = Table(
    'TicketInvoice',
    metadata_obj,
    Column('id', VARCHAR(255), primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('invoiceNumber', VARCHAR(24)),
    Column('user', JSON),
    Column('userId', Integer),
    Column('trip', JSON),
    Column('originStationId', Integer),
    Column('destinationStationId', Integer),
    Column('roundTrip', Boolean),
    Column('qty', Integer),
    Column('amount', Numeric(20, 2)),
    Column('paymentDetails', JSON),
    Column('paymentMethod', JSON),
    Column('paymentMethodId', Integer),
    Column('statusId', Integer),
    Column('options', JSON),
    Column('paymentRefId', VARCHAR(64), default=None),
    Column('expiredAt', TIMESTAMP),
    Column('log', JSON),
    Column('flagId', Integer, default=0),
    Column('ticketCount', Integer, default=0),
    Column('state', VARCHAR(255), default=None),
    Column('deliveryMethodId',Integer),
    Column('deliveryMethod',JSON),
    UniqueConstraint('invoiceNumber', name='IDX_TicketInvoice_invoiceNumber'),
    Index('IDX_TicketInvoice_createdAt', 'createdAt'),
    # Add any additional columns or constraints here
    # ...
)


TicketInvoiceDiscountClaim = Table(
    'TicketInvoiceDiscountClaim',
    metadata_obj,
    Column('id', VARCHAR(255), primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer),
    Column('invoiceId', VARCHAR(255)),
    Column('program', JSON),
    Column('programId', Integer),
    Column('programScenarioId', Integer),
    Column('programRevision', Integer),
    Column('orgUnitId', VARCHAR(8)),
    Column('user', JSON),
    Column('userId', Integer),
    Column('refAmount', Numeric(20, 2)),
    Column('discountAmount', Numeric(20, 2)),
    Column('statusId', BigInteger),
    Column('claimNumber', Integer),
    Column('userClaimNumber', Integer),
    Column('quotaAvailable', Integer),
    Column('log', JSON),
    # Indexes
    Index('IDX_TicketInvoiceDiscountClaim__claimByProgram',
          'programId', 'statusId'),
    Index('IDX_TicketInvoiceDiscountClaim__claimByUser',
          'programId', 'userId', 'statusId'),
    Index('IDX_TicketInvoiceDiscountClaim__lockedClaimByUser',
          'programId', 'userId', 'statusId', 'createdAt'),
    # Add any additional columns or constraints here
    # ...
)


TicketStatus = Table(
    'TicketStatus',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('name', VARCHAR(32)),
    # Add any additional columns or constraints here
    # ...
)


TicketTemplate = Table(
    'TicketTemplate',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer),
    Column('xid', VARCHAR(16)),
    Column('type', Integer),
    Column('statusId', Integer),
    Column('footer', VARCHAR(255), default=None),
    Column('description', Text, default=None),
    # Indexes
    Index('IDX_TicketTemplate_1', 'xid'),
    Index('IDX_TicketTemplate_2', 'statusId'),
    # Add any additional columns or constraints here
    # ...
)


TransactionType = Table(
    'TransactionType',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('name', VARCHAR(32)),
    # Add any additional columns or constraints here
    # ...
)


TripDirection = Table(
    'TripDirection',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('name', VARCHAR(32)),
    # Add any additional columns or constraints here
    # ...
)


TvmDevice = Table(
    'TvmDevice',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON, default=None),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('xid', VARCHAR(6)),
    Column('deviceId', VARCHAR(128)),
    Column('name', VARCHAR(128)),
    Column('stationId', BigInteger, default=None),
    Column('statusId', Integer),
    Column('locationLat', Float, default=None),
    Column('locationLng', Float, default=None),
    Column('locationDescription', Text, default=None),
    Column('boundAt', TIMESTAMP, default=None),
    Column('boundIp', VARCHAR(255), default=None),
    Column('lastConnectedAt', TIMESTAMP, default=None),
    Column('lastConnectedIp', VARCHAR(255), default=None),
    Column('options', JSON),
    # Add any additional columns or constraints here
    # ...
)


User = Table(
    'User',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer),
    Column('xid', VARCHAR(16), default=None),
    Column('fullName', VARCHAR(255), default=None),
    Column('phone', VARCHAR(16), default=None),
    Column('email', VARCHAR(255), default=None),
    Column('age', VARCHAR(32), default=None),
    Column('avatar', VARCHAR(255), default=None),
    Column('statusId', Integer),
    Column('identities', JSON, default=None),
    Column('oldRefId', Integer, default=None),
    Column('roleId', BigInteger),
    # Add any additional columns or constraints here
    # ...
)


UserAuth = Table(
    'UserAuth',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('userId', Integer),
    Column('clientId', VARCHAR(255)),
    Column('clientSecret', JSON),
    Column('statusId', Integer),
    Column('pinWrongCount', Integer, default=0),
    Column('blockedAt', TIMESTAMP),
    Column('blockedUntilAt', TIMESTAMP),
    UniqueConstraint('clientId', name='IDX_UserAuth__clientId')
    # Add any additional columns or constraints here
    # ...
)


UserNotification = Table(
    'UserNotification',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('notificationId', BigInteger),
    Column('notificationXid', VARCHAR(8)),
    Column('userId', BigInteger),
    Column('userXid', VARCHAR(16)),
    Column('hasRead', Boolean, default=False),
    # Add any additional columns or constraints here
    # ...
)


UserOauth = Table(
    'UserOauth',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('userId', Integer),
    Column('fullName', VARCHAR(255)),
    Column('providerRefId', VARCHAR(255)),
    Column('providerToken', Text),
    Column('authProviderId', Integer),
    Column('avatar', VARCHAR(255)),
    # Add any additional columns or constraints here
    # ...
)


UserPaymentAccount = Table(
    'UserPaymentAccount',
    metadata_obj,
    Column('id', VARCHAR(255), primary_key=True),
    Column('createdAt', TIMESTAMP),
    Column('updatedAt', TIMESTAMP),
    Column('metadata', JSON),
    Column('modifiedBy', JSON),
    Column('version', Integer, default=1),
    Column('userId', BigInteger),
    Column('paymentMethodId', BigInteger),
    Column('accountId', VARCHAR(255)),
    Column('options', JSON),
    Column('expiredAt', TIMESTAMP),
    Column('statusId', Integer, default=3),
    Column('authSessionRef', VARCHAR(36)),
    UniqueConstraint('userId', 'paymentMethodId',
                     name='IDX_UserPaymentAccount__uniqueUserPaymentAccount'),
    Index('idx_UserPaymentAccount_accountId', 'paymentMethodId', 'accountId'),
    Index('idx_UserPaymentAccount_authSessionRef', 'authSessionRef')
    # Add any additional columns or constraints here
    # ...
)


# schema_migrations = Table(
#     'schema_migrations',
#     metadata_obj,
#     Column('version', Integer, primary_key=True),
#     Column('dirty', Boolean),
#     # Add any additional columns or constraints here
#     # ...
# )


# spatial_ref_sys = Table(
#     'spatial_ref_sys',
#     metadata_obj,
#     Column('srid', BigInteger, primary_key=True),
#     Column('auth_name', VARCHAR(255)),
#     Column('auth_srid', VARCHAR(255)),
#     Column('srtext', VARCHAR(255)),
#     Column('proj4text', VARCHAR(255)),
#     UniqueConstraint('srid', name='srid')
#     # Add any additional columns or constraints here
#     # ...
# )
