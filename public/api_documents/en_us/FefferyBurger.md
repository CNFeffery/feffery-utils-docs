- id (string; optional):
    The unique id of the component.

- key (string; optional):
    Updates the `key` value of the current component, which can force a re-render of the current component.

- style (dict; optional):
    The CSS styles for the current component.

- className (string; optional):
    The CSS class name for the current component.

- type (a value equal to: 'default', 'squash', 'cross', 'twirl', 'fade', 'slant', 'spiral', 'divide', 'turn', 'pivot', 'sling', 'squeeze', 'spin', 'rotate'; default 'default'):
    The type of icon, with options including `'default'`, `'squash'`, `'cross'`, `'twirl'`, `'fade'`, `'slant'`, `'spiral'`, `'divide'`, `'turn'`, `'pivot'`, `'sling'`, `'squeeze'`, `'spin'`, `'rotate'`. Default value: `'default'`.

- toggled (boolean; optional):
    Sets or listens to the state of the icon.

- size (number; default 32):
    The pixel size of the icon. Default value: `32`.

- direction (a value equal to: 'left', 'right'; default 'left'):
    Available for some types of icons, controls the direction of the animation, with options including `'left'`, `'right'`. Default value: `'left'`.

- duration (number; default 0.3):
    The duration of the animation process, in seconds. Setting it to `0` will disable the animation. Default value: `0.3`.

- distance (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    The size specification of the spacing between horizontal lines of the icon, with options including `'sm'`, `'md'`, `'lg'`. Default value: `'md'`.

- color (string; optional):
    The color of the icon.

- rounded (boolean; default False):
    Whether to render as a rounded rectangle. Default value: `False`.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.
