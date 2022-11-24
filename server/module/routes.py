from flask import request, jsonify
import json
from server import app
from server.module import service


app.route('/api/LightRecord', methods=['GET','POST'])
def handle_lightRecord():
    if(request.method == 'GET'):
        LightRecordResponse = service.getLightRecord()
        return jsonify({
            'state':LightRecordResponse
        }), 200
    elif(request.method == 'POST'):
        LightRecordData = request.get_json()
        LightRecordResponse = service.updateLightRecord(LightRecordData)
        if(int(LightRecordResponse)==0):
            return jsonify({
                'status':'updated',
                'state':LightRecordResponse
            }), 200
        else:
            return 'error'