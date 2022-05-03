from fastapi import FastAPI, Query

from app.algo import SpellingBeeAlgorithm

app = FastAPI()

algo = SpellingBeeAlgorithm()


@app.get("/ping")
def health_check() -> str:
    return "pong"


@app.get("/solve")
async def get_solutions(letters: str = Query(..., min_length=4, max_length=8, example="ABCDEF"),
                        center_letter: str = Query(..., min_length=0, max_length=1, example="G")):
    return algo.solve_for_words(letters=letters, center_letter=center_letter)
