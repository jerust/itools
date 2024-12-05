import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.logger.logger import Logger
from config import host, port, log_config
from src.route.converter import router as converter
from src.route.embedding import router as embedding
from src.route.extractor import router as extractor
from src.route.reranking import router as reranking
from src.route.splitting import router as splitting

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
app.include_router(extractor)
app.include_router(reranking)
app.include_router(splitting)

if __name__ == "__main__":
    print("""
🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰
🥰>> POST /itools/converter/word-to-pdf🥰
🥰>> POST /itools/converter/pdf-to-html🥰
🥰>> POST /itools/extractor/xlsx-reader🥰
🥰>> POST /itools/extractor/docx-reader🥰
🥰>> POST /itools/extractor/pdfx-reader🥰
🥰>> POST /itools/embedding            🥰
🥰>> POST /itools/reranking            🥰
🥰>> POST /itools/splitting            🥰
🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰
""")
    Logger()
    uvicorn.Server(
        uvicorn.Config("itools:app", host=host, port=port, log_config=log_config)
    ).run()
