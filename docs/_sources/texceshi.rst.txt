tex测试
====================

.. raw:: latex

    :file: test.tex


.. raw:: latex

   \\begingroup
   \\sphinxsetup{%
       TitleColor={named}{DarkGoldenrod},
       % pre_border-width is 5.1.0 alias for verbatimborder
       pre_border-width=2pt,
       % pre_padding is 5.1.0 alias for verbatimsep
       pre_padding=5pt,
       % rounded boxes are new at 5.1.0
       pre_border-radius=5pt,
       % TeXcolor means syntax must be as for LaTeX \definecolor
       pre_background-TeXcolor={named}{OldLace},
       pre_border-TeXcolor={named}{Gold},
       %
       % 5.1.0 alias for warningborder
       div.warning_border-width=3pt,
       div.warning_padding=6pt,
       div.warning_padding-right=18pt,
       div.warning_padding-bottom=18pt,
       div.warning_border-TeXcolor={named}{DarkCyan},
       div.warning_background-TeXcolor={named}{LightCyan},
       div.warning_box-shadow=-12pt -12pt inset,
       div.warning_box-shadow-TeXcolor={named}{Cyan},
       %
       % 5.1.0 new name would be div.attention_border-width
       attentionborder=3pt,
       % same as div.attention_border-TeXcolor
       attentionBorderColor={named}{Crimson},
       % same as div.attention_background-TeXcolor
       attentionBgColor={named}{FloralWhite},
       %
       % no CSS-like names yet at 5.1.0 for note-type admonitions
       noteborder=2pt,
       noteBorderColor={named}{Olive},
       hintBorderColor={named}{LightCoral}%
   }
   \\endgroup


.. raw:: latex

   \\setlength{\\parindent}{0pt}