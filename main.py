import random
import string
from http import HTTPStatus

from typing import Optional

from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel

app = FastAPI()

quotes = list()


def get_id():
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


class Quote(BaseModel):
    title: str
    content: str
    about: Optional[str] = None


def find_quote_by_id(qid):
    return list(filter(lambda q: (q['id'] == qid), quotes))


@app.get('/quotes')
async def get_quotes():
    return {"data": quotes}


# @app.get('/quotes/latest')
# async def get_quotes():
#     return {"data": quotes.pop()}


@app.get('/quotes/{qid}')
def get_quote(qid: str):
    quote_found = find_quote_by_id(qid)
    if not quote_found:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f"Quote wth id: {qid} not Found!")
    return {'message': f"Retrieved with id: {qid}",
            'quote': quote_found}


@app.post('/quotes/add', status_code=HTTPStatus.CREATED)
async def add_quote(quote: Quote):
    new_post = quote.dict()
    new_post['id'] = get_id()
    quotes.append(new_post)
    return {"message": "Quote Added!"}


@app.delete('quotes/delete/{id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_quote(qid: str):
    # FIXME make remove work
    quotes.remove(find_quote_by_id(qid))
    return Response(status_code=HTTPStatus.NO_CONTENT)


@app.put('/quotes/update/{id]')
async def update_quote(qid: str, quote: Quote):
    quote_found = find_quote_by_id(qid)
    if not quote_found:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f"Quote wth id: {qid} not Found!")
    # TODO update
    return {'message': f"Updated!"}
