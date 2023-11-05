import streamlit as st

# Drafting a pants with messurmants in python

# Input meshurmants

waist = 98
seat = 102
leg = 81
lower_leg = 44
crotch_length = 23
crotch_circumference = 61
ankle = 36
waistband = 5





#check if all inputs ar given

def check_inputs(waist, seat, leg, lower_leg, crotch_length, crotch_circumference, ankle, waistband):
	'''check_inputs is a funkton to check if all inputs are given if input is missing it print out an error
	
	>>> check_input(1,1,1,1,1,1,1)
	
	inputs are all given
	
	>>> check_input(0,1,1,1,1,1,1)
	
	iput missing error'''
	if waist == 0 :
		print("input missing error")
	elif seat == 0:
		print("input missing error")
	elif leg == 0:
		print("input missing error")
	elif lower_leg == 0:
		print("input missing error")
	elif crotch_length == 0:
		print("input missing error")
	elif crotch_circumference == 0:
		print("input missing error")
	elif ankle == 0:
		print("input missing error")
	elif waistband == 0:
		print("input missing error")
	else:
		print("inputs are all given")

input_statemt = check_inputs(waist, seat, leg, lower_leg, crotch_length, crotch_circumference, ankle, waistband)

print (input_statemt)









#checks if it uses cm or to convert inch in to cm
def inch_or_cm(measuring_tipe_cm):
	'''inch_or_cm checks if the input values are in cm or in inch
		and converts them in to cm if they ar inches, or if they are 
		alrady in cm it multiplys them by 1 to keep them at cm
		
		>>> inch_or_cm(True):
		1
		
		>>> inch_or_cm(Fals)
		2.54'''
	
	if measuring_tipe_cm == True:
		conversion = 1
	else:
		conversion = 2.54
	return(conversion)

conversion_op= inch_or_cm(True)
print("conversion is= " ,conversion_op)






#convert input
def convert_input(waist, seat, leg, lower_leg, crotch_length, crotch_circumference, ankle, waistband):
	'''convert_input takes all the input values an pultiplays them by conversion_op(inch_or_cm)
		wich multiplys with 1 (if the input is alrdy set to cm) or 2.54 (if the input is set to inch)
		>>> convert_input(5)
		5
		>>> convert_input(5)
		12.7'''
	

	waist_op = waist * conversion_op
	seat_op = seat * conversion_op
	lower_leg_op = lower_leg * conversion_op
	crotch_length_op = crotch_length * conversion_op
	crotch_circumference_op = crotch_circumference * conversion_op
	ankle_op = ankle * conversion_op
	waistband_op = waistband * conversion_op
	return(waist_op, seat_op, lower_leg_op, crotch_length_op, crotch_circumference_op, ankle_op, waistband_op)

call_convert_input = convert_input(waist, seat, leg, lower_leg, crotch_length, crotch_circumference, ankle, waistband)

print( "converted val:",call_convert_input[:7])









# converting all inputs to the corisponding lines 

def patern_values(waist_op, seat_op, lower_leg_op, crotch_length_op, crotch_circumference_op, ankle_op, waistband_op):
	'''patern_values takes all converted input values (conver_input) and calculates all the lines of the pants
	patern
	
	>>> patern_values(23 = crotch_length_op)
	a = 23 - 23 * 0.25
	a = 17.25'''
	a = crotch_length_op - crotch_length_op *0.25
	e = seat_op * 0.125 - 1.3
	c = seat_op * 0.125 - 1.3
	g = seat_op * 0.25 + 2.5 - c
	d = c + c * 0.5
	ei2 = c - 1.3
	f = waist_op * 0.25 + 2.5 - ei2
	kj = lower_leg_op
	n = ankle_op *0.25
	o = n
	k  = n * + 2.5
	j = k



	return(a,e,c,g,d,ei2,f,kj,n,o,k,j)
	

	#https://docs.streamlit.io/


#call_patern_values = patern_values()

st.title("Pants Pattern Measuring")

st.markdown("""## This is the Pants Pattern Measuring App.
			Use it to measure pants.
Pleaase input the measurements below.
""")

system = st.toggle(label="acitvate imperial measurements", )

waist = st.text_input(label="waist", value=98)
seat = st.text_input(label="seat")
leg = st.text_input(label="leg")
lower_leg = st.text_input(label="lower_leg")
crotch_length = st.text_input(label="crotch_length")
crotch_circumference = st.text_input(label="crotch_circumference")
ankle = st.text_input(label="ankle")
waistband = st.text_input(label="waistband")

submit = st.button("submit")

if submit:
	st.success("Thank you for submitting your measurements")





