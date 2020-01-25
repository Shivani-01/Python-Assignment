import pickle
o=open('datastore_file.py','wb')
b=datastore={"office":{"medical":[{"roomno":100,"use":"waiting","sq-ft":50,"price":75},{"roomno":101,"use":"waiting","sq-ft":250,"price":75},{"roomno":102,"use":"examination","sq-ft":125,"price":150},{"roomno":103,"use":"examination","sq-ft":125,"price":150},{"roomno":104,"use":"office","sq-ft":150,"price":100}],"parking":{"location":"premium","style":"covered","price":750}}}
pickle.dump(b,o)
o.close()
