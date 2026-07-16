from sqids import Sqids

sqids = Sqids(min_length=5)

def encode_id(*,db_id:int) -> str:
    
    return sqids.encode([db_id])

def decode_code(short_code:str) -> int:
    
    numbers = sqids.decode(short_code) 
    
    return numbers[0] if numbers else None
     


