pending = [4,6,7]
delivered = [1,2,45,200]
all = [5,9,4,6,7,1,2,45,200]

def check_order_status(order_id):
    if order_id in delivered:
        return True
    else:
        return False

def check_order_status_pending(order_id):
    if order_id in pending:
        return True
    else:
        return False

def check_order_status_absent(order_id):
    if order_id not in pending and delivered:
        return True
    else:
        return False

def check_order_add(order_id):
    order_id = delivered.append('45')
    if order_id in delivered:
        return True
    else:
        return False

def add_new_order(order_id):
    order_id = all.append('79')
    if order_id in all:
        return True
    else:
        return False

def order_delivered(order_id):
    order_id = delivered.append('7')
    if order_id in delivered:
        return False
    else:
        return True

