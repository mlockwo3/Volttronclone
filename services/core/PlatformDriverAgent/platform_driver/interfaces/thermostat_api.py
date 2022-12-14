'''
Copyright (c) 2016, Alliance for Sustainable Energy, LLC
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted provided 
that the following conditions are met:
 
1. Redistributions of source code must retain the above copyright notice, this list of conditions 
and the following disclaimer.
 
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions 
and the following disclaimer in the documentation and/or other materials provided with the distribution.
 
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or 
promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND 
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

"""

Thermostat Interface:

API to set and get values for the thermostat over WiFi

FakeThermostat - creates a fake thermostat object
ThermostatInterface - creates a real thermostat obect based on address

-Used with RadioThermostatAgent
version CT50
http://lowpowerlab.com/downloads/RadioThermostat_CT50_Honeywell_Wifi_API_V1.3.pdf

"""

import urllib.request, urllib.error, urllib.parse
from volttron.platform import jsonapi


def Thermostat_API(url):
    ''' Call the interface'''
    return ThermostatInterface(url)

class ThermostatInterface:
    '''Base interface to get and set values on the thermostat
    '''
    def __init__(self, url):
        self.urladdress = url
        self.day_num = {
            'mon' : "0",
            'tue' : "1",
            'wed' : "2",
            'thu' : "3",
            'fri' : "4",
            'sat' : "5",
            'sun' : "6"
        }
        print("Initialized a REAL Thermostat object")

    def t_setpoint(self,data,point,tmode=''):
        ''' Sets cooling setpoint'''
        if tmode == '':
            msg = { point : data }
        else :
            msg = {"tmode": tmode, point : data}
        value = jsonapi.dumps(msg)
        try:
            mode =  (urllib.request.urlopen(self.urladdress,value))
            parsed = jsonapi.loadb(mode.read())
            return jsonapi.dumps(parsed)
        except Exception as parsed:
            return parsed

    def t_cool(self,data):
        ''' Sets cooling setpoint'''
        msg = {"tmode":2,"t_cool":data}
        value = jsonapi.dumps(msg)
        try:
            mode =  (urllib.request.urlopen(self.urladdress,value))
            parsed = jsonapi.loadb(mode.read())
            return jsonapi.dumps(parsed)
        except Exception as parsed:
            return parsed

    def t_heat(self,data):
        ''' Sets heating setpoint'''
        msg = {"tmode":1,"t_heat":data}
        value = jsonapi.dumps(msg)
        try:
            mode =  (urllib.request.urlopen(self.urladdress,value))
            parsed = jsonapi.loadb(mode.read())
            return jsonapi.dumps(parsed)
        except Exception as parsed:
            return parsed

    def over(self,data):
        ''' Sets override controls'''
        msg = {"override":data}
        value = jsonapi.dumps(msg)
        try:
            mode =  (urllib.request.urlopen(self.urladdress,value))
            parsed = jsonapi.loadb(mode.read())
            return jsonapi.dumps(parsed)
        except Exception as parsed:
            return parsed

    def hold(self,data):
        ''' Sets  hold controls'''
        msg = {"hold":data}
        value = jsonapi.dumps(msg)
        try:
            mode =  (urllib.request.urlopen(self.urladdress,value))
            parsed = jsonapi.loadb(mode.read())
            return jsonapi.dumps(parsed)
        except Exception as parsed:
            return parsed

    def model(self):
        ''' Returns device model'''
        address= self.address+"/model"
        try:
            mode =  (urllib.request.urlopen(address))
            parsed = jsonapi.loadb(mode.read())
            return jsonapi.dumps(parsed)
        except Exception as parsed:
            return parsed

    def tstat(self):
        ''' Returns current deicve paramenters'''
        try:
            mode =  (urllib.request.urlopen(self.urladdress))
            parsed = jsonapi.loadb(mode.read())

            return jsonapi.dumps(parsed)

        except Exception as parsed:
            return parsed

    def fmode(self,data):
        ''' Sets fan's mode'''
        msg = {"fmode":data}
        value = jsonapi.dumps(msg)
        try:
            mode =  (urllib.request.urlopen(self.urladdress,value))
            parsed = jsonapi.loadb(mode.read())

            return jsonapi.dumps(parsed)
        except Exception as parsed:
            return parsed

    def mode(self,data):
        ''' Sets  operating mode'''
        msg = {"tmode":data}
        value = jsonapi.dumps(msg)
        try:
            mode =  (urllib.request.urlopen(self.urladdress,value))
            parsed = jsonapi.loadb(mode.read())

            return jsonapi.dumps(parsed)
        except Exception as parsed:
            return parsed

    def energy_led(self,data):
        '''  Controls energy led, possible values: 0,1,2,4'''
        url = self.urladdress+"/led"
        msg = { "energy_led" :int(data)}
        value = jsonapi.dumps(msg)
        try:
            mode =  (urllib.request.urlopen(url,value))
            parsed = jsonapi.loadb(mode.read())

            return jsonapi.dumps(parsed)
        except Exception as parsed:
            return parsed

    def get_heat_pgm(self,day=''):
        ''' get heat program for a week or a specific day
            day = {'mon','tue','wed','thu','fri','sat','sun'}

            for a specific day, say thursday:
            t.get_heat_pgm('thu')

            for a week:
            t.get_heat_pgm()

        '''
        if day =='':
            url = self.urladdress+"/program/heat"
        else:
            url = self.urladdress+"/program/heat/"+str(day)
        try:
            mode =  (urllib.request.urlopen(url))
            parsed = jsonapi.loadb(mode.read())

            return jsonapi.dumps(parsed)

        except Exception as parsed:
            return parsed

    def get_cool_pgm(self,day=''):
        ''' get cool program for a week or a specific day
            day = {'mon','tue','wed','thu','fri','sat','sun'}

            for a specific day, say thursday:
            t.get_cool_pgm('thu')

            for a week:
            t.get_cool_pgm()

        '''
        if day =='':
            url = self.urladdress+"/program/cool"
        else:
            url = self.urladdress+"/program/cool/"+str(day)
        try:
            mode =  (urllib.request.urlopen(url))
            parsed = jsonapi.loadb(mode.read())

            return jsonapi.dumps(parsed)

        except Exception as parsed:
            return parsed

    def set_cool_pgm(self,schedules,day=''):
        ''' set cool program for a week or a specific day
            day = {'mon','tue','wed','thu','fri','sat','sun'}

            for a spefic day, say 'thu'
            t.set_cool_pgm('{"360, 80, 480, 80, 1080, 80, 1320 , 80",'thu')

            t.set_cool_pgm('{
                        "1": [360, 70, 480, 70, 1080, 70, 1320, 70],
                        "0": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "3": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "2": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "5": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "4": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "6": [360, 66, 480, 58, 1080, 66, 1320, 58]
                 }')
        '''
        schedule = str(schedules)
        if day =='':
            url = self.urladdress+"/program/cool"
            try:

                mode =  (urllib.request.urlopen(url,jsonapi.dumps(schedules)))
                parsed = jsonapi.loadb(mode.read())

                return jsonapi.dumps(parsed)
            except Exception as parsed:
                return parsed
        else:
            url = self.urladdress+"/program/cool/"+str(day)
            try:
                schedule_str = {}
                schedule_str = { str(self.day_num[day]): [int(e) if e.isdigit() else e for e in schedule.split(',')]}

                mode =  (urllib.request.urlopen(url,jsonapi.dumps(schedule_str)))
                parsed = jsonapi.loadb(mode.read())

                return jsonapi.dumps(parsed)
            except Exception as parsed:
                return parsed

    def set_heat_pgm(self,schedules,day=''):
        """
        set heat program for a week or a specific day
        day = {'mon','tue','wed','thu','fri','sat','sun'}

        for a spefic day, say 'thu'

        .. code-block:: python

            t.set_heat_pgm('{"360, 80, 480, 80, 1080, 80, 1320 , 80",'thu')

        for a week

        .. code-block:: python

            t.set_heat_pgm('{
                        "1": [360, 70, 480, 70, 1080, 70, 1320, 70],
                        "0": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "3": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "2": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "5": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "4": [360, 66, 480, 58, 1080, 66, 1320, 58],
                        "6": [360, 66, 480, 58, 1080, 66, 1320, 58]
                 }')
        """
        schedule = str(schedules)
        if day =='':
            url = self.urladdress+"/program/heat"
            try:

                mode =  (urllib.request.urlopen(url, jsonapi.dumps(schedules)))
                parsed = jsonapi.loadb(mode.read())
                return jsonapi.dumps(parsed)
            except Exception as parsed:
                return parsed

        else:
            url = self.urladdress+"/program/heat/"+str(day)

            try:
                schedule_str = {}
                schedule_str = { str(self.day_num[day]): [int(e) if e.isdigit() else e for e in schedule.split(',')]}
                mode =  (urllib.request.urlopen(url,jsonapi.dumps(schedule_str)))
                parsed = jsonapi.loadb(mode.read())
                return jsonapi.dumps(parsed)
            except Exception as parsed:
                return parsed
