
def validate_tracking(tracking):
    valid_tracking = "SAG-26-CTS-SPK-000527-2"
    return tracking == valid_tracking

def show_status():
    print("\nTracking Found!")
    print("Status: 空港で保留 (On Hold at Airport)")
    print("Location: New Chitose Airport Sales Office")
    print("Delivery Status: Not Delivered")
    print("Estimated Delivery: Pending Clearance")

def main():
    print("Sagawal Express Tracking System")
    tracking = input("Enter Tracking Number: ")
    
    if validate_tracking(tracking):
        show_status()
    else:
        print("Invalid Tracking Number")

if __name__ == "__main__":
    main()
