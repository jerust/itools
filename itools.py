import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.logger.logger import Logger
from config import host, port, log_config
from src.route.converter import router as converter
from src.route.embedding import router as embedding
from src.route.reranker import router as reranker
from src.route.splitter import router as splitter
from src.route.office import router as office

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(converter)
app.include_router(embedding)
app.include_router(reranker)
app.include_router(splitter)
app.include_router(office)

if __name__ == "__main__":
    print("""
🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰
🥰>> POST /itools/converter/word-to-pdf🥰
🥰>> POST /itools/converter/pdf-to-html🥰
🥰>> POST /itools/office/excel-reader  🥰
🥰>> POST /itools/office/docx-reader   🥰
🥰>> POST /itools/office/pdf-reader    🥰
🥰>> POST /itools/embedding            🥰
🥰>> POST /itools/reranker             🥰
🥰>> POST /itools/splitter             🥰
🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰
""")
    Logger()
    uvicorn.Server(
        uvicorn.Config("itools:app", host=host, port=port, log_config=log_config)
    ).run()
