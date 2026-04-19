from crewai_tools import BaseTool, SerperDevTool, DirectoryReadTool, FileReadTool
from pydantic import BaseModel, Field
from textblob import TextBlob

class SentimentSchema(BaseModel):
    text: str = Field(..., description="The email draft text to analyze.")

class AdvancedSentimentTool(BaseTool):
    name: str = "Outreach Tone Analyzer"
    description: str = "Analyzes email drafts for professional tone and sentiment."
    args_schema: type[BaseModel] = SentimentSchema

    def _run(self, text: str) -> str:
        """
        Runs the sentiment analysis logic using TextBlob.
        """
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0.5:
            sentiment = "Extremely Positive / Enthusiastic"
        elif polarity > 0.1:
            sentiment = "Positive / Professional"
        elif polarity > -0.1:
            sentiment = "Neutral"
        else:
            sentiment = "Negative / Potentially Aggressive"
            
        return f"The sentiment is {sentiment} (Polarity Score: {polarity:.2f})"

def get_directory_read_tool():
    return DirectoryReadTool(directory='./instructions')

def get_file_read_tool():
    return FileReadTool()

def get_search_tool():
    return SerperDevTool()

def get_sentiment_tool():
    return AdvancedSentimentTool()
