from FlaskHelper import Mapper, MapperMethod
import Sample, SampleDto, FeatureData, Feature, FeatureDataDto
import DefaultValues

@Mapper()
class SampleMapper:

    @MapperMethod(requestClass=[SampleDto.SampleRequestDto, [Feature.Feature], int().__class__], responseClass=Sample.Sample)
    def fromPostRequestDtoToModel(self, dto, featureList, value, key, model) :
        self.validator.sample.listLengthAreEqualsInSampleMapping(featureList, model.featureDataList)
        model.key = key
        model.featureDataList = []
        self.overrideValues(dto, featureList, value, model)
        return model

    @MapperMethod(requestClass=[[FeatureDataDto.FeatureDataRequestDto], str().__class__])
    def overrideFeatureDataRequestDtoValues(self, featureDataList, key) :
        for featureData in featureDataList :
            if not featureData.sampleKey :
                featureData.sampleKey = key

    @MapperMethod(requestClass=[SampleDto.SampleRequestDto, [Feature.Feature], Sample.Sample])
    def overrideFeatureData(self, dto, featureList, model):
        model.label = dto.label
        for feature in featureList :
            featureData = self.helper.featureData.getRespectiveFeatureDataByFeature(feature, model.featureDataList)
            if not featureData :
                featureData = FeatureData.FeatureData()
                featureData.sample = model
            featureData.feature = feature

    @MapperMethod(requestClass=[SampleDto.SampleRequestDto, [Feature.Feature], int().__class__, Sample.Sample])
    def overrideValues(self, dto, featureList, value, model, patchValues=False):
        model.label = dto.label
        for feature in featureList :
            featureData = self.helper.featureData.getRespectiveFeatureDataByFeature(feature, model.featureDataList)
            if not featureData :
                featureData = FeatureData.FeatureData()
                featureData.sample = model
                featureData.feature = feature
            self.service.sample.patchDataValues(featureData, value, patchValues=patchValues)
        self.service.sample.patchSampleValues(model, value, patchValues=patchValues)
