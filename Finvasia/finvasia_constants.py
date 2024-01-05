PRODUCT_MIS = "I"
PRODUCT_CNC = "C"
PRODUCT_NRML = "M"
PRODUCT_CO = "H"

# Order types
ORDER_TYPE_MARKET = "MKT"
ORDER_TYPE_LIMIT = "LMT"
ORDER_TYPE_SLM = "SL-MKT"
ORDER_TYPE_SL = "SL-LMT"

# Varities
VARIETY_REGULAR = "regular"
VARIETY_CO = "co"
VARIETY_AMO = "amo"
VARIETY_ICEBERG = "iceberg"
VARIETY_AUCTION = "auction"

# Transaction type
TRANSACTION_TYPE_BUY = "B"
TRANSACTION_TYPE_SELL = "S"

# Validity
VALIDITY_DAY = "DAY "
VALIDITY_IOC = "IOC"
VALIDITY_TTL = "TTL"

# Position Type
POSITION_TYPE_DAY = "day"
POSITION_TYPE_OVERNIGHT = "overnight"

# Exchanges
EXCHANGE_NSE = "NSE"
EXCHANGE_BSE = "BSE"
EXCHANGE_NFO = "NFO"
EXCHANGE_CDS = "CDS"
EXCHANGE_BFO = "BFO"
EXCHANGE_MCX = "MCX"
EXCHANGE_BCD = "BCD"


# Status constants
STATUS_COMPLETE = "COMPLETE"
STATUS_REJECTED = "REJECTED"
STATUS_CANCELLED = "CANCELED"
STATUS_TRIGGER_PENDING = "TRIGGER_PENDING"
STATUS_MODIFIED = "Replaced"
STATUS_OPEN = "OPEN"

# instruments
BANKNIFTY = "BANKNIFTY"
NIFTY = "NIFTY"
DATA_BANKNIFTY = "NIFTY BANK"
DATA_NIFTY = "NIFTY 50"
INDICES = "INDICES"

# contract types
CALL = "CE"
PUT = "PE"

# general constants
MAX_REQUEST_TRY = 2
TRADINGSYMBOL = 'tsym'
STRIKE = 'strike'
CE = "CE"
PE = "PE"
EXPIRY = "expiry"
TOKEN = "token"
ENCTOKEN = "enctoken"
_default_timeout = 7   # in seconds
kite_header_version = "3"
OHLC_TIME = "Time"
OHLC_OPEN = "Open"
OHLC_HIGH = "High"
OHLC_LOW = "Low"
OHLC_CLOSE = "Close"
OHLC_VOLUME = "Volume"
LAST_PRICE = "last_price"
LPP_ERROR_STRING = "17070 The Price is out of the current execution range"
VOLUNTARY_CLOSEOUT = "16795 Order cancelled due to voluntary close out"
INVAILD_TOKEN = "Session Expired :  Invalid Session Key"
TAG = 'remarks'
ORDER_ID = 'norenordno'
STATUS = 'stat'
ORDER_STATUS = 'status'
STATUS_ERROR = 'Not_Ok'
STATUS_SUCCESS = 'Ok'
ORDER_TYPE = 'prctyp'
EXCHANGE = 'exch'
AVERAGE_PRICE = 'avgprc'
QTY = 'qty'
PRC = 'prc'
PRODUCT = 'prd'
TRANTYPE = 'trantype'
BASKETLISTS = 'basketlists'
REJECTION_REASON = 'rejreason'
TRIGGER_PRICE = 'trgprc'