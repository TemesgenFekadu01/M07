from dataclasses import dataclass, field
import datetime

class Order:
    '''Order Class'''
    def __init__(self, OrderID, CustomerID, SalespersonPersonID, PickedByPersonID, ContactPersonID, BackorderOrderID, OrderDate, ExpectedDeliverDate,
    CustomerPurchaseOrderNumber, IsUndersupplyBackordered, Comments, DeliveryInstructions, InternalComments, PickingCompletedWhen, LastEditedBy, LastEditedWhen):
        self.oid = OrderID
        self.cid = CustomerID
        self.spid = SalespersonPersonID
        self.pbpid = PickedByPersonID
        self.cpid = ContactPersonID
        self.boid = BackorderOrderID
        self.od = OrderDate
        self.edd = ExpectedDeliverDate
        self.cpon = CustomerPurchaseOrderNumber
        self.iub = IsUndersupplyBackordered
        self.c = Comments
        self.di = DeliveryInstructions
        self.ic = InternalComments
        self.pcw = PickingCompletedWhen
        self.leb = LastEditedBy
        self.lew = LastEditedWhen
    
    def __gt__(self, other):
        return self.od > other.od

    def __ge__(self, other):
        return self.od >= other.od

@dataclass
class Customer:
    OrderID: int
    CustomerID: int
    SalespersonPersonID: int
    PickedByPersonID: int
    ContactPersonID: int
    BackorderOrderID: int
    OrderDate: datetime.date
    ExpectedDeliverDate: datetime.date
    CustomerPurchaseOrderNumber: str
    IsUndersupplyBackordered: bool
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    PickingCompletedWhen: datetime.datetime
    LastEditedBy: int
    LastEditedWhen: datetime.datetime

    def __gt__(self, other):
        return self.od > other.od
    
    def __ge__(self, other):
        return self.od >= other.od

class Invoice:
    '''Invoice Class'''
    def __init__(self, InvoiceID, CustomerID, BillToCustomerID, OrderID, DeliveryMethodID, ContactPersonID, AccountsPersonID, SalespersonPersonID, PackedByPersonID,
    InvoiceDate, CustomerPurchaseOrderNumber, IsCreditNote, CreditNoteReason, Comments, DeliveryInstructions, InternalComments, TotalDryItems, TotalChillerItems,
    DeliveryRun, RunPosition, ReturnedDeliveryData, ConfirmedDeliveryTime, ConfirmedReceivedBy, LastEditedBy, LastEditedWhen):
        self.iid = InvoiceID
        self.cid = CustomerID
        self.btcid = BillToCustomerID
        self.oid = OrderID
        self.dmid = DeliveryMethodID
        self.cpid = ContactPersonID
        self.apid = AccountsPersonID
        self.spid = SalespersonPersonID
        self.pbpid = PackedByPersonID
        self.id = InvoiceDate
        self.cpon = CustomerPurchaseOrderNumber
        self.icn = IsCreditNote
        self.cnr = CreditNoteReason
        self.c = Comments
        self.di = DeliveryInstructions
        self.ic = InternalComments
        self.tdi = TotalDryItems
        self.tci = TotalChillerItems
        self.dr = DeliveryRun
        self.rp = RunPosition
        self.rdd = ReturnedDeliveryData
        self.cdt = ConfirmedDeliveryTime
        self.crb = ConfirmedReceivedBy
        self.leb = LastEditedBy
        self.lew = LastEditedWhen

    def __gt__(self, other):
        return self.id > other.id

    def __ge__(self, other):
        return self.id >= other.id

@dataclass
class Invoice:
    InvoiceID: int
    CustomerID: int
    BillToCustomerID: int
    OrderID: int
    DeliveryMethodID: int
    ContactPersonID: int
    AccountsPersonID: int
    SalespersonPersonID: int
    PackedByPersonID: int
    InvoiceDate: datetime.date
    CustomerPurchaseOrderNumber: str
    IsCreditNote: bool
    CreditNoteReason: str
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    TotalDryItems: int
    TotalChillerItems: int
    DeliveryRun: str
    RunPosition: str
    ReturnedDeliveryData: str
    ConfirmedDeliveryTime: datetime.datetime
    ConfirmedReceivedBy: str
    LastEditedBy: int
    LastEditedWhen: datetime.datetime

    def __gt__(self, other):
        return self.id > other.id

    def __ge__(self, other):
        return self.id >= other.id

class Customer:
    '''Customer Class'''
    def __init__(self, CustomerID, CustomerName, BillToCustomerID, CustomerCategoryID, BuyingGroupID, PrimaryContactPersonID, AlternateContactPersonID, DeliveryMethod,
    DeliveryCityId, PostalCityID, CreditLimit, AccountOpenedDate, StandardDiscountPercentage, IsStatementSent, IsOnCreditHold, PaymentDays, PhoneNumber, FaxNumber,
    DeliveryRun, RunPosition, WebsiteURL, DeliveryAddressLine1, DeliveryAddressLine2, DeliveryPostalCode, DeliveryLocation, PostalAddressLine1, PostalAddressLine2,
    PostalPostalCode, LastEditedBy, ValidFrom, ValidTo):
        self.cid = CustomerID
        self.cn = CustomerName
        self.btcid = BillToCustomerID
        self.ccid = CustomerCategoryID
        self.bgid = BuyingGroupID
        self.pcpid = PrimaryContactPersonID
        self.acpid = AlternateContactPersonID
        self.dm = DeliveryMethod
        self.dcid = DeliveryCityId
        self.pcid = PostalCityID
        self.cl = CreditLimit
        self.aod = AccountOpenedDate
        self.sdp = StandardDiscountPercentage
        self.iss = IsStatementSent
        self.ioch = IsOnCreditHold
        self.pd = PaymentDays
        self.pn = PhoneNumber
        self.fn = FaxNumber
        self.dr = DeliveryRun
        self.rp = RunPosition
        self.wu = WebsiteURL
        self.dal1 = DeliveryAddressLine1
        self.dal2 = DeliveryAddressLine2
        self.dpc = DeliveryPostalCode
        self.dl = DeliveryLocation
        self.pal1 = PostalAddressLine1
        self.pal2 = PostalAddressLine2
        self.ppc = PostalPostalCode
        self.leb = LastEditedBy
        self.vf = ValidFrom
        self.vt = ValidTo

@dataclass
class Customer:
    CustomerID: int
    CustomerName: str
    BillToCustomerID: int
    CustomerCategoryID: int
    BuyingGroupID: int
    PrimaryContactPersonID: int
    AlternateContactPersonID: int
    DeliveryMethod: int
    DeliveryCityId: int
    PostalCityID: int
    CreditLimit: float
    AccountOpenedDate: datetime.date
    StandardDiscountPercentage: float
    IsStatementSent: bool
    IsOnCreditHold: bool
    PaymentDays: int
    PhoneNumber: str
    FaxNumber: str
    DeliveryRun: str
    RunPosition: str 
    WebsiteURL: str
    DeliveryAddressLine1: str
    DeliveryAddressLine2: str
    DeliveryPostalCode: str
    DeliveryLocation: str
    PostalAddressLine1: str
    PostalAddressLine2: str
    PostalPostalCode: str
    LastEditedBy: int
    ValidFrom: datetime.datetime
    ValidTo: datetime.datetime