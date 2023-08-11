import pika, json

#upload to mongodb and create message in rabbitmq
def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        return "internal server error", 503
    
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"]
    }
    
    try:
        channel.basic_publish(
            exchange="",
            routing_key="video", # name of queue
            body=json.dumps(message), # can we use jsonify here?
            properties=pika.BasicProperties(
                deliver_mode=pika.spec.PERSISTENT_DELIVERY_MODE # make queue durable, messages are retained even in case of crash
            )
        )
    except:
        fs.delete(fid)
        return "internal server error", 503