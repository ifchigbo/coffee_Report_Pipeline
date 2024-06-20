from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy import String
from databaseConnection import Base
from typing import List, Dict, cast
from pydantic import BaseModel
from sqlalchemy.orm import Session
from databaseConnection import get_db
from databaseConnection import engine
import models

Base.metadata.create_all(bind=engine)


app = FastAPI()

#Route pull all contacts
@app.get("/getcontacts")
async def getContacts(db: Session = Depends(get_db)):
    print("I got here")
    try:
        query = db.query(models.CrmContact).all()
        print(db.query(models.CrmContact))
        if query is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data record not found")
        return{"Result" : query}
    except Exception as e:
        print(e)
        return {"Message" : HTTPException(status_code=status.HTTP_404_NOT_FOUND)}
#Route get unique phone numbers
@app.get("/getcontacts/{p_number}")
async def contactPhoneNumber(p_number:str, db: Session = Depends(get_db)):
    try:
        result = db.query(models.CrmContact.first_name, models.CrmContact.last_name).filter(models.CrmContact.phone_number == p_number).all()
        print(result)
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")
        return {"Details" : result}
    except Exception as e:
        print(e)
        return{"Error": HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server may be offline")}

#Route for all Opened Cases
@app.get("/retrievestatus/{case_status}")
async def getCaseStatus(case_status: str,db: Session = Depends(get_db)):
    try:
        #query = db.query(models.CrmCase).filter(models.CrmCase.case_object['case']['status'] == case_status)
        query = db.query(models.CrmCase).filter(
            models.CrmCase.case_object['case'].op('->>')('status') == case_status
        )
        result_set = query.all()
        print(query)
        #result_set = db.query(models.CrmCase).all()
        if not result_set :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="result set not found")
        return{"Data": result_set}
    except Exception as e:
        print(e)
        return{"Error": HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)}

#Get all Closed Cases
#include the description of the Case in the return statement
@app.get("/getclosed/{closed_case}")
async def getClosedCases(closed_case: str, db: Session = Depends(get_db)):
    try:
        query = db.query(models.CrmCase.case_object).filter(models.CrmCase.case_object['case'].op('->>')('status') == closed_case)
        result_set = query.all()

        if not result_set:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

        print(list(result_set[0])[0]['case']['description'])
        count = 0
        descriptions = []
        while count < len(result_set):
            print(result_set[count][0]['case']['description'])
            descriptions.append(result_set[count][0]['case']['description'])
            count +=1

        return{"Data" : result_set,
               "Case Descriptions" : descriptions}

    except Exception as e:
        print(e)
        return{"Messaage" : HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Connection Closed")}


#Search Cases by  CaseID for Return Requests -> Gets the Complete case record

@app.get("/cases/count")
async  def GetCaseCount(db: Session = Depends(get_db)):
    try:
        query = db.query(models.CrmCase.ticket_id).count()
        if query is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items not found")
        return {"Message" : query}
    except Exception as e:
        print(e)
        return {"Message": HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection Timed Out")}
@app.get("/cases/{case_id}")
async def getCasesbyId(case_id: str, db:Session = Depends(get_db)):
    try:
        query = db.query(models.CrmCase).filter(models.CrmCase.ticket_id == case_id)
        query_result = query.all()
        if query_result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return {"Data":query_result}
    except Exception as e:
        print(e)
        return{"Message":HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection Timed Out")}

#Get Case Resolution by Ticket ID -> Case Resolution Record by ID
@app.get("/cases/resolution/{case_id}")
async def getResolutionbyID(case_id:str, db: Session = Depends(get_db)):
    try:
        query = db.query(models.CrmCase.case_object['case']['resolution']).filter(models.CrmCase.ticket_id == case_id)
        query_result = query.scalar()
        print(query)

        if query_result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found ..... ")
        return{"Data" :  query_result}
    except Exception as e:
        print(e)
        return {"Message" : HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail="Connection Timed Out")}