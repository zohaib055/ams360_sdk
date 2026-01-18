from dataclasses import asdict, dataclass, fields, is_dataclass
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any, ClassVar, Dict, List, Optional

def _serialize_value(value: Any) -> Any:
    if isinstance(value, RequestModel):
        return value.to_dict()
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, list):
        return [_serialize_value(item) for item in value]
    if isinstance(value, dict):
        return {k: _serialize_value(v) for k, v in value.items()}
    return value

@dataclass
class RequestModel:
    __field_map__: ClassVar[Dict[str, str]] = {}

    def to_dict(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}
        for f in fields(self):
            value = getattr(self, f.name)
            if value is None:
                continue
            key = self.__field_map__.get(f.name, f.name)
            data[key] = _serialize_value(value)
        return data

@dataclass
class BankGetByCodeRequest(RequestModel):
    BankCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class BrokerGetByCodeRequest(RequestModel):
    BrokerCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class BrokerGetByShortNameRequest(RequestModel):
    BrokerShortName: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class BrokerGetListByLastNamePrefixRequest(RequestModel):
    BrokerLastNamePrefix: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class ClaimGetByIdRequest(RequestModel):
    ClaimId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class ClaimGetListByCustomerIdRequest(RequestModel):
    CustomerId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class ClaimGetListByPolicyIdRequest(RequestModel):
    PolicyId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CommonNoteInsertRequest(RequestModel):
    CommonNote: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CommonSuspenseDeleteRequest(RequestModel):
    SuspenseId: Optional[str] = None
    SuspenseTypeId: Optional[str] = None
    SuspenseType: Optional[int] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CommonSuspenseGetBySuspenseIdRequest(RequestModel):
    SuspenseId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CommonSuspenseGetListByEntityIdRequest(RequestModel):
    EntityId: Optional[str] = None
    IsCompleted: Optional[bool] = None
    EntityType: Optional[int] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CommonSuspenseInsertRequest(RequestModel):
    CommonSuspense: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CommonSuspenseUpdateRequest(RequestModel):
    CommonSuspense: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CompanyGetByCodeRequest(RequestModel):
    CompanyCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CompanyGetByShortNameRequest(RequestModel):
    CompanyShortName: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CompanyGetListByNamePrefixRequest(RequestModel):
    CompanyNamePrefix: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CompanyGetListByParentCompanyCodeRequest(RequestModel):
    ParentCompanyCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CompanyGetListByTypeRequest(RequestModel):
    CompanyTypes: Optional[List[str]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerActivityInsertRequest(RequestModel):
    CustomerActivity: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerGetByIdRequest(RequestModel):
    CustomerId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerGetByNumberRequest(RequestModel):
    CustomerNumber: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerGetListByNamePrefixRequest(RequestModel):
    NamePrefix: Optional[str] = None
    CustomerType: Optional[str] = None
    IsBrokersCustomer: Optional[bool] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerInsertRequest(RequestModel):
    Customer: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerNoteInsertRequest(RequestModel):
    CustomerNote: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerServicePersonnelGetListRequest(RequestModel):
    CustomerId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerServicePersonnelModifyListRequest(RequestModel):
    CustomerId: Optional[str] = None
    ModifyList: Optional[List[Dict[str, Any]]] = None
    DeleteList: Optional[List[Dict[str, Any]]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerSuspenseDeleteRequest(RequestModel):
    SuspenseId: Optional[str] = None
    CustomerId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerSuspenseGetBySuspenseIdRequest(RequestModel):
    SuspenseId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerSuspenseGetListByCustomerIdRequest(RequestModel):
    CustomerId: Optional[str] = None
    IsComplete: Optional[bool] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerSuspenseInsertRequest(RequestModel):
    Suspense: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerSuspenseUpdateRequest(RequestModel):
    Suspense: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class CustomerUpdateRequest(RequestModel):
    Customer: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class EmployeeGetByCodeRequest(RequestModel):
    EmployeeCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class EmployeeGetByShortNameRequest(RequestModel):
    EmployeeShortName: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class EmployeeGetListByLastNamePrefixRequest(RequestModel):
    EmployeeLastNamePrefix: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class EmployeeGetListByTypeRequest(RequestModel):
    IncludeRepresentative: Optional[bool] = None
    IncludeExecutive: Optional[bool] = None
    IncludeSalesCenterRepresentative: Optional[bool] = None
    IncludeOther: Optional[bool] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class EmployeeInsertRequest(RequestModel):
    Employee: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class EmployeeUpdateRequest(RequestModel):
    Employee: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class FileChunkBeginRequest(RequestModel):
    NumberOfChunks: Optional[int] = None
    TotalBytes: Optional[int] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class FileChunkEndRequest(RequestModel):
    DocStageId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class FileChunkSendRequest(RequestModel):
    FileChunk: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLBranchGetByCodeRequest(RequestModel):
    GLBranchCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLBranchGetByShortNameRequest(RequestModel):
    GLBranchShortName: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLBranchGetListByGLDivisionCodeRequest(RequestModel):
    GLDivisionCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLBranchGetListByNamePrefixRequest(RequestModel):
    GLBranchNamePrefix: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLDepartmentGetByCodeRequest(RequestModel):
    GLDepartmentCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLDepartmentGetByShortNameRequest(RequestModel):
    GLDepartmentShortName: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLDepartmentGetListByGLBranchCodeRequest(RequestModel):
    GLBranchCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLDepartmentGetListByNamePrefixRequest(RequestModel):
    GLDepartmentNamePrefix: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLDivisionGetByCodeRequest(RequestModel):
    GLDivisionCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLDivisionGetByShortNameRequest(RequestModel):
    GLDivisionShortName: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLDivisionGetListByNamePrefixRequest(RequestModel):
    GLDivisionNamePrefix: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLGroupGetByCodeRequest(RequestModel):
    GLGroupCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLGroupGetByShortNameRequest(RequestModel):
    GLGroupShortName: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLGroupGetListByGLDepartmentCodeRequest(RequestModel):
    GLDepartmentCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class GLGroupGetListByNamePrefixRequest(RequestModel):
    GLGroupNamePrefix: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class LineOfBusinessGetByCodeRequest(RequestModel):
    LineOfBusinessCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class LineOfBusinessGetListRequest(RequestModel):
    TypeOfBusinessCode: Optional[int] = None
    IncomeGroup: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class LoginRequest(RequestModel):
    AgencyNo: Optional[str] = None
    LoginId: Optional[str] = None
    Password: Optional[str] = None
    EmployeeCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PersonalNoteGetListRequest(RequestModel):
    DateFrom: Optional[datetime] = None
    DateTo: Optional[datetime] = None
    PurgeDateFrom: Optional[datetime] = None
    PurgeDateTo: Optional[datetime] = None
    IncludeOnlyAttachments: Optional[bool] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PersonalNoteInsertRequest(RequestModel):
    UserNote: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PlanTypeGetByCodeRequest(RequestModel):
    PlanCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PlanTypeGetListByCompanyCodeRequest(RequestModel):
    CompanyCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PolicyCorrectRequest(RequestModel):
    Policy: Optional[Dict[str, Any]] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PolicyEndorseRequest(RequestModel):
    PolicyId: Optional[str] = None
    TransactionEffectiveDate: Optional[datetime] = None
    TransactionType: Optional[str] = None
    TransactionDescription: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PolicyGetListByCustomerIdRequest(RequestModel):
    CustomerId: Optional[str] = None
    PolicyStatus: Optional[List[str]] = None
    IncludeMultiEntity: Optional[bool] = None
    IncludeAccountingSubType: Optional[bool] = None
    IncludeSubmissionSubType: Optional[bool] = None
    IncludePolicySubType: Optional[bool] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PolicyGetListByCustomerNumberRequest(RequestModel):
    CustomerNumber: Optional[str] = None
    PolicyStatus: Optional[List[str]] = None
    IncludeMultiEntity: Optional[bool] = None
    IncludeAccountingSubType: Optional[bool] = None
    IncludeSubmissionSubType: Optional[bool] = None
    IncludePolicySubType: Optional[bool] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PolicyGetListByPolicyNumberAndDateRequest(RequestModel):
    PolicyNumber: Optional[str] = None
    InEffectOnDate: Optional[datetime] = None
    IncludeMultiEntity: Optional[bool] = None
    IncludeAccountingSubType: Optional[bool] = None
    IncludeSubmissionSubType: Optional[bool] = None
    IncludePolicySubType: Optional[bool] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PolicyGetListByPolicyNumberRequest(RequestModel):
    PolicyNumber: Optional[str] = None
    PolicyEffectiveDate: Optional[datetime] = None
    PolicyExpirationDate: Optional[datetime] = None
    IncludeMultiEntity: Optional[bool] = None
    IncludeAccountingSubType: Optional[bool] = None
    IncludeSubmissionSubType: Optional[bool] = None
    IncludePolicySubType: Optional[bool] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class PolicyGetRequest(RequestModel):
    PolicyId: Optional[str] = None
    TransactionEffectiveDate: Optional[datetime] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class SearchByPhoneNumberRequest(RequestModel):
    PhoneNumber: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class ValueListGetRequest(RequestModel):
    ListName: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class VendorGetByCodeRequest(RequestModel):
    VendorCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class VendorGetListByIsCompanyRequest(RequestModel):
    IsCompany: Optional[bool] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class VendorGetListByLastNamePrefixRequest(RequestModel):
    VendorLastNamePrefix: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class VendorInvoiceGetByIdRequest(RequestModel):
    VendorInvoiceId: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

@dataclass
class VendorInvoiceGetListByVendorRequest(RequestModel):
    VendorCode: Optional[str] = None
    __field_map__: ClassVar[Dict[str, str]] = {}

