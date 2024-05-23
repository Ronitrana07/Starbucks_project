print("Starbucks")

print("Menu- Starbucks Coffee Company")

Cold_cups="a"
Iced_teas="b"
Hot_teas="c"
Hot_drinks="d"


x=str(input("Menu:-\n(a)Cold_cups:, \n(b)Iced_teas:, \n(c)Hot_teas:, \n(d)Hot_drinks:,\nSelect the option= "))
if x=="a":
	print("Menu/Cold cups")
	w1=str(input("Cold cups menu:-\n(a)White siren bling plastic cold cup/ 900 \n(b)Plastic reusable Cold Cup with Lid & staw/600 \n(c)Siren logo plastic Cold Cup/1200 \nEnter the option you want="))
	if w1=="a":
		print("Thankyou for ordering the White siren bling plastic cold cup")
		print("Less 5%:-",900*0.05)
		print("Final amount:-", 900-900*0.05)
	if w1=="b":
		print("Thankyou for ordering the plastic reusable cold cup with Lid & straw :")
		print("Less 5%:-", 600*0.05)
		print("Final amount:-", 600-600*0.05)
	if w1=="c":
		print("Thankyou for ordering the Siren logo plastic Cold Cup")
		print("Less 5%:-", 1200*0.05)
		print("Final amount:-", 1200-1200*0.05)
elif x=="b":
	print("Menu/Iced teas")
	w2=str(input("Iced teas menu:- \n(a)Black iced tea/569 \n(b)Green iced tea/899 \n(c)Oolong iced tea/1200 \nSelect the option= "))
	if w2=="a":
		print("Thankyou for ordering the Black iced tea:")
		print("Less 5%:-", 569*0.05)
		print("Final amount:-", 569-569*0.05)	
	if w2=="b":
		print("Thankyou for ordering the Green iced tea:")
		print("Less 5%:-", 899*0.05)
		print("Final amount:-", 899-899*0.05)
	if w2=="c":
		print("Thankyou for ordering the Oolong iced tea:")
		print("Less 5%:-", 1200*0.05)
		print("Final amount:-", 1200-1200*0.05)
elif x=="c":
	print("Menu/Hot teas")
	w3=str(input("Hot teas menu:- \n(a)Chai tea \n(b)Black tea \n(c)Green tea \nSelect the option= "))
	if w3=="a":
		print("You select Chai tea")
		c1=str(input("Chai tea menu:- \n(a)Chai tea lattle/499 \n(b)Chai tea/249 \nSelect the option= "))
		if c1=="a":
			print("Thankyou for ordering the Chai tea lattle:")
			print("Less 5%:-", 499*0.05)
			print("Final amount:-", 499-499*0.05)
		if c1=="b":
			print("Thankyou for ordering the Chai tea lattle:")
			print("Less 5%:-", 249*0.05)
			print("Final amount:-", 249-299*0.05)    	
	if w3=="b":
		print("You select Black tea")
		b1=str(input("Black tea menu:-\n(a)Earl grey tea/849 \n(b)Teavana london fog tea latte/1600 \n(c)Royal english breakfast tea/1259 \nSelect the option= "))		
		if b1=="a":
			print("Thankyou for ordering the Earl grey tea lattle:")
			print("Less 5%:-", 849*0.05)
			print("Final amount:-", 849-849*0.05)
		if b1=="b":
			print("Thankyou for ordering the Teavana london fog tea lattle:")
			print("Less 5%:-", 1600*0.05)
			print("Final amount:-", 1600-1600*0.05)	
		if b1=="c":
			print("Thankyou for ordering The Royal english breakfast tea lattle:")
			print("Less 5%:-", 1259*0.05)
			print("Final amount:-", 1259-1259*0.05)
	if w3=="c":
		print("You select Green tea")
		G1=str(input("Green tea menu:-\n(a)Emperors clouds and mist/1600 \n(b)Matcha tea latte/1259 \n(c)Honey citrus mint tea/1359 \nSelect the option= "))
		if G1=="a":
			print("Thankyou for ordering the Emperors clouds and mist:")
			print("Less 5%:-", 1600*0.05)
			print("Final amount:-", 1600-1600*0.05)
		if G1=="b":
			print("Thankyou for ordering the Matcha tea latte:")
			print("Less 5%:-", 1259*0.05)
			print("Final amount:-", 1259-1259*0.05)
		if G1=="c":
			print("Thankyou for ordering the Honey citrus mint tea:")
			print("Less 5%:-", 1359*0.05)
			print("Final amount:-", 1359-1359*0.05)
elif x=="d":
	print("Menue/Hot drinks")
	h1=str(input("Hot drinks menu:- \n(a)Hot buttered Rum/669 \n(b)Mulled cider/999 \n(c)Cafe au lait/1239 \nSelect the option= "))
	if h1=="a":
		print("Thankyou for ordering the Hot buttered rum:")
		print("Less 5%:-", 669*0.05)
		print("Final amount:-", 669-669*0.05)
	if h1=="b":
		print("Thankyou for ordering the Mulled cider:")
		print("Less 5%:-", 999*0.05)
		print("Final amount:-", 999-999*0.05)
	if h1=="c":
		print("Thankyou for ordering the Cafe au lait:")
		print("Less 5%:-", 1239*0.05)
		print("Final amount:-", 1239-1239*0.05)

 

