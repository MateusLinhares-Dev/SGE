import os
from products.models import Product
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache, SQLiteCache
import logging

logger = logging.getLogger(__name__)

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.2
)

set_llm_cache(SQLiteCache('sge_project/db_response_products.db'))

def chabot_specialist_ia(pergunta):
    """
    Gera resposta a partir dos dados do banco de produtos disponiveis no estoque
    """
    try:
        logger.info("Iniciando geração de código...")

        products = Product.objects.all()
        product = {
            p.id: {
                "title": p.title,
                "brand": p.brand.name,
                "category": p.category.name,
                "selling_price":p.selling_price,
                "quantity": p.quantity
            } 
            for p in products
            }

        product_sge = (
            PromptTemplate.from_template(
                """
                Você é um especialista que irá responder perguntas sobre o estoque de produtos para o usuário
                seu objetivo é usar como base a lista de informações do produtos e responder ao usuário de forma direta.
                produtos: {produtos}
                pergunta: {pergunta}
                """
            )
            | model
            | StrOutputParser()
        )

        response_llm_product = product_sge.invoke({'produtos':product, 'pergunta': pergunta})

        return response_llm_product
    except Exception as e:
        logger.error(f"Erro ao gerar código: {str(e)}")
        return f"Erro ao gerar código: {str(e)}"