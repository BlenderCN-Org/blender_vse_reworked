keyconfig_data = \
[("Sequencer",
  {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
  {"items":
   [("sequencer.select_all",
     {"type": 'A', "value": 'PRESS'},
     {"properties":
      [("action", 'SELECT'),
       ],
      },
     ),
    ("sequencer.select_all",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("action", 'DESELECT'),
       ],
    "active":False,
      },
     ),
    ("sequencer.select_all",
     {"type": 'I', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("action", 'INVERT'),
       ],
      },
     ),
    ("sequencer.select_all",
     {"type": 'A', "value": 'DOUBLE_CLICK'},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("sequencer.cut",
     {"type": 'K', "value": 'PRESS'},
     {"properties":
      [("type", 'SOFT'),
       ],
    "active":False,
      },
     ),
    ("sequencer.cut",
     {"type": 'K', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'HARD'),
       ],
    "active":False,
      },
     ),
    ("sequencer.mute",
     {"type": 'H', "value": 'PRESS'},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("sequencer.mute",
     {"type": 'H', "value": 'PRESS', "shift": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("sequencer.unmute",
     {"type": 'H', "value": 'PRESS', "alt": True},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("sequencer.unmute",
     {"type": 'H', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("sequencer.lock", {"type": 'L', "value": 'PRESS', "shift": True}, None),
    ("sequencer.unlock", {"type": 'L', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("sequencer.reassign_inputs", {"type": 'R', "value": 'PRESS'}, None),
    ("sequencer.reload", {"type": 'R', "value": 'PRESS', "alt": True}, None),
    ("sequencer.reload",
     {"type": 'R', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("adjust_length", True),
       ],
      },
     ),
    ("sequencer.offset_clear", {"type": 'O', "value": 'PRESS', "alt": True}, None),
    ("sequencer.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
    ("sequencer.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.images_separate", {"type": 'Y', "value": 'PRESS'}, None),
    ("sequencer.meta_toggle", {"type": 'TAB', "value": 'PRESS'}, None),
    ("sequencer.meta_make", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.meta_separate", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("sequencer.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
    ("sequencer.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
    ("sequencer.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
    ("sequencer.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("sequencer.strip_jump",
     {"type": 'PAGE_UP', "value": 'PRESS'},
     {"properties":
      [("next", True),
       ("center", False),
       ],
      },
     ),
    ("sequencer.strip_jump",
     {"type": 'PAGE_DOWN', "value": 'PRESS'},
     {"properties":
      [("next", False),
       ("center", False),
       ],
      },
     ),
    ("sequencer.strip_jump",
     {"type": 'PAGE_UP', "value": 'PRESS', "alt": True},
     {"properties":
      [("next", True),
       ("center", True),
       ],
      },
     ),
    ("sequencer.strip_jump",
     {"type": 'PAGE_DOWN', "value": 'PRESS', "alt": True},
     {"properties":
      [("next", False),
       ("center", True),
       ],
      },
     ),
    ("sequencer.swap",
     {"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True},
     {"properties":
      [("side", 'LEFT'),
       ],
      },
     ),
    ("sequencer.swap",
     {"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True},
     {"properties":
      [("side", 'RIGHT'),
       ],
      },
     ),
    ("sequencer.gap_remove",
     {"type": 'BACK_SPACE', "value": 'PRESS'},
     {"properties":
      [("all", False),
       ],
      },
     ),
    ("sequencer.gap_remove",
     {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True},
     {"properties":
      [("all", True),
       ],
      },
     ),
    ("sequencer.gap_insert", {"type": 'EQUAL', "value": 'PRESS', "shift": True}, None),
    ("sequencer.snap", {"type": 'S', "value": 'PRESS', "shift": True}, None),
    ("sequencer.swap_inputs", {"type": 'S', "value": 'PRESS', "alt": True}, None),
    ("sequencer.cut_multicam",
     {"type": 'ONE', "value": 'PRESS'},
     {"properties":
      [("camera", 1),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'TWO', "value": 'PRESS'},
     {"properties":
      [("camera", 2),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'THREE', "value": 'PRESS'},
     {"properties":
      [("camera", 3),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'FOUR', "value": 'PRESS'},
     {"properties":
      [("camera", 4),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'FIVE', "value": 'PRESS'},
     {"properties":
      [("camera", 5),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'SIX', "value": 'PRESS'},
     {"properties":
      [("camera", 6),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'SEVEN', "value": 'PRESS'},
     {"properties":
      [("camera", 7),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'EIGHT', "value": 'PRESS'},
     {"properties":
      [("camera", 8),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'NINE', "value": 'PRESS'},
     {"properties":
      [("camera", 9),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'ZERO', "value": 'PRESS'},
     {"properties":
      [("camera", 10),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS'},
     {"properties":
      [("extend", False),
       ("linked_handle", False),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("extend", True),
       ("linked_handle", False),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True},
     {"properties":
      [("extend", False),
       ("linked_handle", True),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("extend", True),
       ("linked_handle", True),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("extend", False),
       ("linked_handle", False),
       ("left_right", 'MOUSE'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("extend", True),
       ("linked_handle", False),
       ("left_right", 'NONE'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.select_linked_pick",
     {"type": 'L', "value": 'PRESS'},
     {"properties":
      [("extend", False),
       ],
      },
     ),
    ("sequencer.select_linked_pick",
     {"type": 'L', "value": 'PRESS', "shift": True},
     {"properties":
      [("extend", True),
       ],
      },
     ),
    ("sequencer.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("sequencer.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
    ("sequencer.select_channel", {"type": 'C', "value": 'PRESS'}, None),
    ("sequencer.slip", {"type": 'S', "value": 'PRESS'}, None),
    ("wm.context_set_int",
     {"type": 'O', "value": 'PRESS', "alt": True},
     {"properties":
      [("data_path", 'scene.sequence_editor.overlay_frame'),
       ("value", 0),
       ],
      },
     ),
    ("transform.seq_slide", {"type": 'G', "value": 'PRESS'}, None),
    ("transform.seq_slide", {"type": 'EVT_TWEAK_R', "value": 'ANY'}, None),
    ("transform.transform",
     {"type": 'E', "value": 'PRESS'},
     {"properties":
      [("mode", 'TIME_EXTEND'),
       ],
      },
     ),
    ("marker.add", {"type": 'M', "value": 'PRESS'}, None),
    ("marker.rename", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
    ("wm.call_menu",
     {"type": 'V', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'SEQUENCER_MT_view'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'S', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'SEQUENCER_MT_select'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'E', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'SEQUENCER_MT_edit'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'T', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'SEQUENCER_MT_transform'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'I', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'SEQUENCER_MT_strip'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'N', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'SEQUENCER_MT_navigation'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'M', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'SEQUENCER_MT_marker'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'A', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'SEQUENCER_MT_add'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'D', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'SEQUENCER_MT_add'),
       ],
      },
     ),
    ("render.opengl",
     {"type": 'F10', "value": 'PRESS'},
     {"properties":
      [("sequencer", True),
       ],
      },
     ),
    ("render.opengl",
     {"type": 'F10', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("animation", True),
       ("sequencer", True),
       ],
      },
     ),
    ("sound.mixdown", {"type": 'F10', "value": 'PRESS', "shift": True}, None),
    ("sequencer.select",
     {"type": 'F', "value": 'PRESS', "shift": True},
     {"properties":
      [("left_right", 'RIGHT'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'F', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("left_right", 'LEFT'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select_handles",
     {"type": 'R', "value": 'PRESS'},
     {"properties":
      [("side", 'BOTH'),
       ],
      },
     ),
    ("sequencer.select_handles",
     {"type": 'R', "value": 'PRESS', "shift": True},
     {"properties":
      [("side", 'RIGHT'),
       ],
      },
     ),
    ("sequencer.select_handles",
     {"type": 'R', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("side", 'LEFT'),
       ],
      },
     ),
    ("sequencer.select_time_cursor", {"type": 'F', "value": 'PRESS'}, None),
    ("sequencer.select_active_side",
     {"type": 'C', "value": 'PRESS', "alt": True},
     {"properties":
      [("side", 'LEFT'),
       ],
      },
     ),
    ("sequencer.select_active_side",
     {"type": 'C', "value": 'PRESS', "shift": True},
     {"properties":
      [("side", 'RIGHT'),
       ],
      },
     ),
    ("sequencer.ripple_delete", {"type": 'V', "value": 'PRESS'}, None),
    ("transform.transform",
     {"type": 'G', "value": 'PRESS'},
     {"properties":
      [("mode", 'TRANSLATION'),
       ],
      },
     ),
    ("sequencer.show_waveform_selected_sounds", {"type": 'W', "value": 'PRESS'}, None),
    ("sequencer.toggle_all_modifiers", {"type": 'W', "value": 'PRESS', "shift": True}, None),
    ("sequencer.preview_selected", {"type": 'P', "value": 'PRESS', "shift": True}, None),
    ("sequencer.set_preview_range",
     {"type": 'I', "value": 'PRESS'},
     {"properties":
      [("type", 'IN'),
       ],
      },
     ),
    ("sequencer.set_preview_range",
     {"type": 'O', "value": 'PRESS'},
     {"properties":
      [("type", 'OUT'),
       ],
      },
     ),
    ("sequencer.split_extract",
     {"type": 'K', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'LEFT'),
       ],
      },
     ),
    ("sequencer.split_extract",
     {"type": 'K', "value": 'PRESS', "alt": True},
     {"properties":
      [("direction", 'RIGHT'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'SEQUENCER_MT_add'),
       ],
      },
     ),
    ("sequencer.split_lift",
     {"type": 'K', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("direction", 'LEFT'),
       ],
      },
     ),
    ("sequencer.split_lift",
     {"type": 'K', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("direction", 'RIGHT'),
       ],
      },
     ),
    ("sequencer.zoom_vertical",
     {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'IN'),
       ],
      },
     ),
    ("sequencer.delete_lift", {"type": 'DEL', "value": 'PRESS'}, None),
    ("sequencer.delete_lift", {"type": 'X', "value": 'PRESS'}, None),
    ("sequencer.zoom_vertical",
     {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'OUT'),
       ],
      },
     ),
    ("view2d.zoom_in", {"type": 'NUMPAD_6', "value": 'PRESS', "ctrl": True}, None),
    ("view2d.zoom_out", {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.split",
     {"type": 'K', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'HARD'),
       ],
      },
     ),
    ("sequencer.split",
     {"type": 'K', "value": 'PRESS'},
     {"properties":
      [("type", 'SOFT'),
       ],
      },
     ),
    ("sequencer.match_frame", {"type": 'F', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("sequencer.extend_to_fill", {"type": 'E', "value": 'PRESS', "shift": True}, None),
    ("sequencer.move",
     {"type": 'NUMPAD_8', "value": 'PRESS', "shift": True},
     {"properties":
      [("direction", 'UP'),
       ],
      },
     ),
    ("sequencer.move",
     {"type": 'NUMPAD_2', "value": 'PRESS', "shift": True},
     {"properties":
      [("direction", 'DOWN'),
       ],
      },
     ),
    ("sequencer.move",
     {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True},
     {"properties":
      [("direction", 'LEFT'),
       ],
      },
     ),
    ("sequencer.move",
     {"type": 'NUMPAD_6', "value": 'PRESS', "shift": True},
     {"properties":
      [("direction", 'RIGHT'),
       ],
      },
     ),
    ("screen.frame_offset",
     {"type": 'NUMPAD_1', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("screen.frame_offset",
     {"type": 'NUMPAD_3', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("screen.frame_offset",
     {"type": 'NUMPAD_7', "value": 'PRESS'},
     {"properties":
      [("delta", -25),
       ],
      },
     ),
    ("screen.frame_offset",
     {"type": 'NUMPAD_9', "value": 'PRESS'},
     {"properties":
      [("delta", 25),
       ],
      },
     ),
    ("screen.animation_play", {"type": 'NUMPAD_6', "value": 'PRESS'}, None),
    ("screen.animation_play",
     {"type": 'NUMPAD_4', "value": 'PRESS'},
     {"properties":
      [("reverse", True),
       ],
      },
     ),
    ("sequencer.concatenate", {"type": 'V', "value": 'PRESS', "shift": True}, None),
    ("sequencer.jogshuttle", {"type": 'J', "value": 'PRESS'}, None),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(os.path.splitext(os.path.basename(__file__))[0], keyconfig_data)
