FROM python: 3.11

RUN pip install pandas
RUN pip install flask
RUN pip install scikit-learn
RUN pip install xgboost
RUN pip install joblib

RUN mkdir /app
COPY xgb_model_jl /app/.
COPY xg_model_api.py /app/.
RUN cd /app
CMD [“python”, “/app/xg_model_app.py”]