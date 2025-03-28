#include "max_distance_timeout_number.h"

namespace esphome {
namespace LD2401P {

void MaxDistanceTimeoutNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_basic_config();
}

}  // namespace LD2401P
}  // namespace esphome
