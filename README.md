# PxL-AutoPylot

Autopilot your Windows inputs by monitoring pixels on your screen.

This tool allows you to automate your actions with no code but a configuration file following this sample :
```json
{
  "window_name": "Window name",
  "description": "This is a simple description",
  "debug": true,
  "automations": [
    {
      "pixel": { "x": 1065, "y": 126 },
      "color": { "r": 188, "g": 24, "b": 62 },
      "target_color": false,
      "actions": [
        { "action_type": "key", "args": { "key": "1" } },
        { "action_type": "key", "args": { "key": "2" } }
      ]
    },
    {
      "pixel": { "x": 900, "y": 126 },
      "color": { "r": 188, "g": 24, "b": 62 },
      "target_color": false,
      "actions": [
        { "action_type": "stop", "args": { "message": "stop message." } }
      ]
    }
  ]
}
```
## Autopilot

| key | type | description |
| --- | ----------- | ------ |
| window_name | `string` | Window name to target.
| description | `string` | Description regarding your goal. Does nothing.
| debug | `boolean` | Whether you want to print debugging information.
| automations | `Array<Automation>` | List of your automations. See `Automation` below.

## Automation

| key | type | description |
| --- | ----------- | ------ |
| pixel | `Pixel` | Pixel you want to monitor.
| pixel.x | `int` | X (horizontal) coordinate of your pixel.
| pixel.y | `int` | Y (vertical) coordinate of your pixel.
| color | `Color` | Color you want to compare with your target pixel.
| color.r | `int` | Red byte of your color.
| color.g | `int` | Green byte of your color.
| color.b | `int` | Blue byte of your color.
| target_color | `boolean` | `true` if you want your actions to be triggered when the pixel meets the given color.<br>`false` if you want your actions to be triggered when the pixel is different from the given color.
| actions | `Array<Action>` | List of your actions. See `Action` below. 

## Action 

| key | type | description |
| --- | ----------- | ------ |
| action_type | `Enum<ActionType>` | Action your want to execute.<br>`key` : Press & release a key.<br>`key_press` : Press a key.<br>`key_release` : Release a key.<br>`click` : Click and release the left mouse button.<br>`click_press` : Click the left mouse button.<br>`click_release` : Release the left mouse button.<br>`move` : Move the mouse.<br>`stop` : Stop the autopilot. To be use as a stop condition. |
| args | `{}` | Given args to your action.
| args.key | `string` | Key argument. **Only for keyboard actions.**
| args.x | `int` | X (horizontal) coordinate argument. **Only for mouse actions.**
| args.y | `int` | Y (vertical) coordinate argument. **Only for mouse actions.**
| args.message | `string` | Message argument. **Only for stop action.**