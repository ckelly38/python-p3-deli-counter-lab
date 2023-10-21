def line(katz_deli):
    if (katz_deli == None or len(katz_deli) < 1):
        print("The line is currently empty.");
    else:
        fpart = "The line is currently: ";
        mystrpt = "";
        for i in range(len(katz_deli)):
            mystrpt += str(i + 1) + ". " + katz_deli[i];
            if (i + 1 < len(katz_deli)): mystrpt += " ";
            else: pass;
        print(fpart + mystrpt);
    return None;

def take_a_number(katz_deli, name):
    #this adds them to the list and returns the list.
    #print(f"Welcome, {name}. You are number {num} in line.");
    #insert at the front, then use pop to remove
    if (katz_deli == None or name == None or len(name) < 1): return None;
    else: pass;
    myfi = -1;
    for i in range(len(katz_deli)):
        if (katz_deli[i] == name):
            myfi = i;
            break;
        else: pass;
    if (myfi < 0 or len(katz_deli) - 1 < myfi):
        katz_deli.append(name);
        print(f"Welcome, {name}. You are number {len(katz_deli)} in line.");
    else: print(f"Welcome, {name}. You are number {(myfi + 1)} in line.");
    return katz_deli;

def now_serving(katz_deli):
    if (katz_deli == None or len(katz_deli) < 1):
        print("There is nobody waiting to be served!");
        return [];
    else:
        print(f"Currently serving {katz_deli[0]}.");
        katz_deli.remove(katz_deli[0]);
        return katz_deli;
