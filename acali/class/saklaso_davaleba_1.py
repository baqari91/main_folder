
from homeassistant.core import HomeAssistant
from homeassistant.const import STATE_ON, STATE_OFF

class LightController:
    def __init__(self, hass):
        self.hass = hass

    def turn_on_light(self, entity_id):
        try:
            self.hass.services.call('light', 'turn_on', {'entity_id': entity_id})
            print(f"Turned on {entity_id}.")
        except Exception as e:
            print(f"Failed to turn on {entity_id}: {e}")

    def turn_off_light(self, entity_id):
        try:
            self.hass.services.call('light', 'turn_off', {'entity_id': entity_id})
            print(f"Turned off {entity_id}.")
        except Exception as e:
            print(f"Failed to turn off {entity_id}: {e}")

    def get_light_status(self, entity_id):
        try:
            state = self.hass.states.get(entity_id)
            if state is not None:
                if state.state == STATE_ON:
                    print(f"{entity_id} is currently on.")
                elif state.state == STATE_OFF:
                    print(f"{entity_id} is currently off.")
                else:
                    print(f"Unknown state for {entity_id}: {state.state}")
            else:
                print(f"Entity {entity_id} not found.")
        except Exception as e:
            print(f"Failed to get status of {entity_id}: {e}")

# Example usage:
# Initialize Home Assistant
hass = HomeAssistant()
# Authenticate or set up connection to your Home Assistant instance

# Initialize LightController
light_controller = LightController(hass)

# Example usage of methods
# light_controller.turn_on_light('your_entity_id')
# light_controller.turn_off_light('your_entity_id')
# light_controller.get_light_status('your_entity_id')

# Remember to handle authentication and establish a proper connection to your Home Assistant instance before using these methods.
