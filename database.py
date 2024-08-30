from sqlalchemy import create_engine, text
connection_string = "mysql+pymysql://41YyTG48WpguXMQ.root:5L4yCMvjMQXqkKzb@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/chaos"
engine = create_engine(connection_string, connect_args={
    "ssl":{
    "ssl_ca" : "<CA_PATH>"
}
})

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())