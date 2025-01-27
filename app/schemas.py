from pydantic import BaseModel
from datetime import datetime

class TransferHistoryRequest(BaseModel):
    RequestID: str
    RequestDate: datetime
    RequestTransactionCode: str
    SrvCtrNo: str
    TelNo: str
    UID: str
    DocomoID: str
    ServiceCode: str
    ExecMode: str
    TransfereeCode: str
    TargetMonth: str
    GetPerPage: int
    PageNo: int

class TransferHistoryResponse(BaseModel):
    ProcessNumber: str
    ProcessTime: datetime
    ProcessType: str
    SourceCommonIDGr: str
    DestinationCommonIDGr: str
    PointCount: int
    Result: dict