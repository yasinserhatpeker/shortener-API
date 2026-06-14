from sqids import Sqids

sqids = Sqids(min_length=5)

def encode_id(*,db_id:int) -> str:
    
    return sqids.encode([db_id]) # get the db_id and converts to 5-length short code

def decode_code(short_code:str) -> int:
    
    numbers=sqids.decode(short_code) # get the short_code and converts to db_id 
    
    return numbers[0] if numbers else None
     

# this two function is bidirectional (two-way binding)

