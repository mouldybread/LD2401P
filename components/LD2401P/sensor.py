import esphome.codegen as cg
from esphome.components import sensor
import esphome.config_validation as cv
from esphome.const import (
    DEVICE_CLASS_DISTANCE,
    UNIT_CENTIMETER,
    UNIT_PERCENT,
    CONF_LIGHT,
    DEVICE_CLASS_ILLUMINANCE,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_SIGNAL,
    ICON_FLASH,
    ICON_MOTION_SENSOR,
    ICON_LIGHTBULB,
    UNIT_LUX,
)
from . import CONF_LD2401P_ID, LD2401PComponent

DEPENDENCIES = ["LD2401P"]
CONF_MOVING_DISTANCE = "moving_distance"
CONF_STILL_DISTANCE = "still_distance"
CONF_MOVING_ENERGY = "moving_energy"
CONF_STILL_ENERGY = "still_energy"
CONF_DETECTION_DISTANCE = "detection_distance"
CONF_MOVE_ENERGY = "move_energy"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_LD2401P_ID): cv.use_id(LD2401PComponent),
        cv.Optional(CONF_MOVING_DISTANCE): sensor.sensor_schema(
            device_class=DEVICE_CLASS_DISTANCE,
            unit_of_measurement=UNIT_CENTIMETER,
            icon=ICON_SIGNAL,
        ),
        cv.Optional(CONF_STILL_DISTANCE): sensor.sensor_schema(
            device_class=DEVICE_CLASS_DISTANCE,
            unit_of_measurement=UNIT_CENTIMETER,
            icon=ICON_SIGNAL,
        ),
        cv.Optional(CONF_MOVING_ENERGY): sensor.sensor_schema(
            unit_of_measurement=UNIT_PERCENT,
            icon=ICON_MOTION_SENSOR,
        ),
        cv.Optional(CONF_STILL_ENERGY): sensor.sensor_schema(
            unit_of_measurement=UNIT_PERCENT,
            icon=ICON_FLASH,
        ),
        cv.Optional(CONF_LIGHT): sensor.sensor_schema(
            device_class=DEVICE_CLASS_ILLUMINANCE,
            icon=ICON_LIGHTBULB,
            unit_of_measurement=UNIT_PERCENT
        ),
        cv.Optional(CONF_DETECTION_DISTANCE): sensor.sensor_schema(
            device_class=DEVICE_CLASS_DISTANCE,
            unit_of_measurement=UNIT_CENTIMETER,
            icon=ICON_SIGNAL,
        ),
    }
)

CONFIG_SCHEMA = CONFIG_SCHEMA.extend(
    {
        cv.Optional(f"g{x}"): cv.Schema(
            {
                cv.Optional(CONF_MOVE_ENERGY): sensor.sensor_schema(
                    unit_of_measurement=UNIT_PERCENT,
                    entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                    icon=ICON_MOTION_SENSOR,
                ),
                cv.Optional(CONF_STILL_ENERGY): sensor.sensor_schema(
                    unit_of_measurement=UNIT_PERCENT,
                    entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                    icon=ICON_FLASH,
                ),
            }
        )
        for x in range(14)
    }
)


async def to_code(config):
    LD2401P_component = await cg.get_variable(config[CONF_LD2401P_ID])
    if moving_distance_config := config.get(CONF_MOVING_DISTANCE):
        sens = await sensor.new_sensor(moving_distance_config)
        cg.add(LD2401P_component.set_moving_target_distance_sensor(sens))
    if still_distance_config := config.get(CONF_STILL_DISTANCE):
        sens = await sensor.new_sensor(still_distance_config)
        cg.add(LD2401P_component.set_still_target_distance_sensor(sens))
    if moving_energy_config := config.get(CONF_MOVING_ENERGY):
        sens = await sensor.new_sensor(moving_energy_config)
        cg.add(LD2401P_component.set_moving_target_energy_sensor(sens))
    if still_energy_config := config.get(CONF_STILL_ENERGY):
        sens = await sensor.new_sensor(still_energy_config)
        cg.add(LD2401P_component.set_still_target_energy_sensor(sens))
    if light_config := config.get(CONF_LIGHT):
        sens = await sensor.new_sensor(light_config)
        cg.add(LD2401P_component.set_light_sensor(sens))
    if detection_distance_config := config.get(CONF_DETECTION_DISTANCE):
        sens = await sensor.new_sensor(detection_distance_config)
        cg.add(LD2401P_component.set_detection_distance_sensor(sens))
    for x in range(14):
        if gate_conf := config.get(f"g{x}"):
            if move_config := gate_conf.get(CONF_MOVE_ENERGY):
                sens = await sensor.new_sensor(move_config)
                cg.add(LD2401P_component.set_gate_move_sensor(x, sens))
            if still_config := gate_conf.get(CONF_STILL_ENERGY):
                sens = await sensor.new_sensor(still_config)
                cg.add(LD2401P_component.set_gate_still_sensor(x, sens))
