import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light, output
from esphome.const import CONF_OUTPUT_ID, CONF_COLD_WHITE, CONF_WARM_WHITE, \
    CONF_AMBER, CONF_COLD_WHITE_COLOR_TEMPERATURE, CONF_WARM_WHITE_COLOR_TEMPERATURE, \
    CONF_AMBER_COLOR_TEMPERATURE

wwa_ns = cg.esphome_ns.namespace('wwa')
WWALightOutput = wwa_ns.class_('WWALightOutput', light.LightOutput)

CONF_CONSTANT_BRIGHTNESS = 'constant_brightness'

CONFIG_SCHEMA = light.RGB_LIGHT_SCHEMA.extend({
    cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(WWALightOutput),
    cv.Required(CONF_COLD_WHITE): cv.use_id(output.FloatOutput),
    cv.Required(CONF_WARM_WHITE): cv.use_id(output.FloatOutput),
    cv.Required(CONF_AMBER): cv.use_id(output.FloatOutput),
    cv.Required(CONF_COLD_WHITE_COLOR_TEMPERATURE): cv.color_temperature,
    cv.Required(CONF_WARM_WHITE_COLOR_TEMPERATURE): cv.color_temperature,
    cv.Required(CONF_AMBER_COLOR_TEMPERATURE): cv.color_temperature,
    cv.Optional(CONF_CONSTANT_BRIGHTNESS, default=False): cv.boolean,
})


def to_code(config):
    var = cg.new_Pvariable(config[CONF_OUTPUT_ID])
    yield light.register_light(var, config)
    cwhite = yield cg.get_variable(config[CONF_COLD_WHITE])
    cg.add(var.set_cold_white(cwhite))
    cg.add(var.set_cold_white_temperature(config[CONF_COLD_WHITE_COLOR_TEMPERATURE]))

    wwhite = yield cg.get_variable(config[CONF_WARM_WHITE])
    cg.add(var.set_warm_white(wwhite))
    cg.add(var.set_warm_white_temperature(config[CONF_WARM_WHITE_COLOR_TEMPERATURE]))
    
    amber = yield cg.get_variable(config[CONF_AMBER])
    cg.add(var.set_amber(amber))
    cg.add(var.set_amber_temperature(config[CONF_AMBER_COLOR_TEMPERATURE]))
    cg.add(var.set_constant_brightness(config[CONF_CONSTANT_BRIGHTNESS]))
