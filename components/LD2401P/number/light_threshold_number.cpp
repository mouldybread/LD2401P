#include "light_threshold_number.h"

namespace esphome {
namespace LD2401P {

void LightThresholdNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_light_out_control();
}

}  // namespace LD2401P
}  // namespace esphome
