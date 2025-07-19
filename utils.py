import re
def parse_financial_data(text) -> dict:
    # Split the text into lines
    lines = text.strip().split('\n')
    
    data = {}
    current_field = None
    
    for line in lines:
        # Check if this line is a field name
        if not re.match(r'^[\d,.+%]+$', line.strip()): 
            current_field = line.strip()
            data[current_field] = []
        else:
            # This line contains a value
            value = line.strip().rstrip('%')  # Remove % sign if present
            value = value.replace(',', '')  # Remove commas
            
            if current_field:
                data[current_field].append(value)
    
    return data
def parse_cashflow_data(text) -> dict:
    # Split the text into lines
    lines = text.strip().split('\n')
    # print("lines\n",lines)
    data = {}
    current_field = None
    count =0
    for line in lines:
        # Check if this line is a field name
        if  re.match(r'^[A-Za-z\s]+$', line): 
            current_field = line.strip()
            data[current_field] = []
        else:
            # This line contains a value
            value = line.strip().rstrip('%')  # Remove % sign if present
            value = value.replace(',', '')  # Remove commas
    
            
            if current_field:
                data[current_field].append(value)
        
    return data