from FlaskHelper import Controller, ControllerMethod
import SampleDto, HttpStatus

@Controller(url = '/samples')
class SampleController:

    @ControllerMethod(url='/<key>', requestClass=SampleDto.SampleRequestDto)
    def post(self, dto, key):
        return self.service.sample.create(dto, key), HttpStatus.CREATED

    @ControllerMethod(url='/<key>')
    def get(self, key=None):
        return self.service.sample.queryByKey(key), HttpStatus.OK

    @ControllerMethod(url='/<key>', requestClass=SampleDto.SampleRequestDto)
    def put(self, dto, key):
        return self.service.sample.update(dto, key), HttpStatus.ACCEPTED

    @ControllerMethod(url='/<key>/<value>', requestClass=SampleDto.SampleRequestDto)
    def patch(self, dto, key, value):
        return self.service.sample.patch(dto, key, int(value)), HttpStatus.ACCEPTED

    @ControllerMethod(url='/<key>')
    def delete(self, key):
        self.service.sample.delete(key), HttpStatus.NO_CONTENT
        return {}, HttpStatus.NO_CONTENT


@Controller(url = '/samples/batch')
class SampleBatchController:

    @ControllerMethod()
    def get(self):
        return self.service.sample.queryAll(), HttpStatus.OK
