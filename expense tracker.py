#expense tracker

print("$$ expense tracker $$")

total=0

n=int(input("\nhow many expense do you want to enter:"))

for i in range(n):
    print(f"\n---expense{i+1}---")

    name=input("enter expense name:")
    
    amount=int(input("enter amount:rs"))

    total=total+amount

    print("\n=======================")
    
    print(f"total expense:rs{total}")
    
    print("\n=======================")
