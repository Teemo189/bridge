toolbox学习
====================

**详细内容**



.. rest-example::
    .. collapse:: A Different Label
        :class: custom-summary
        :name: summary0

        Something else that might escape notice.

登录 `桥梁检测管理系统 <http://bridge.jianlide.cn/v/login.html>`__ ,看到的是系统主页,这里分为6个部分的信息展示。

进入 `toolbox学习内容 <file:///C:/Users/Administrator/Desktop/bridge/build/html/toolbox.html>`__ ,看到的是系统主页,这里分为6个部分的信息展示。

.. collapse:: 更多操作

    浏览量  评论  收藏  分享


**本地文件链接**

:asset:`hello_world.txt`

:asset:`hello_world <hello_world.txt>`

:download:`hello_world.txt <./assets/hello_world.txt>`

.. only:: builder_html

    :download:`this example script <./assets/hello_world.txt>`

**版本控制**

.. versionadded:: 2.4
.. versionadded:: 2.5  The *spam* parameter.

.. versionadded:: 2.6
    The *parrot* parameter.

.. deprecated:: 3.1
    Use :func:`spam` instead.

.. deprecated:: 3.2  Use :func:`lobster` instead.

.. versionremoved:: 1.2.3  Use :func:`foo` instead.

.. versionremoved:: 1.2.3

    Due to an unfixable bug this function has been removed.
    If you desperately need this functionality please write to the mailing list at

.. versionchanged:: 0.3.0

    * Parameters for ``__init__`` can be documented either in the class docstring
      or alongside the attribute.
      The class docstring has priority.
    * Added support for `autodocsumm <https://github.com/Chilipp/autodocsumm>`_.

**代码**

.. code-block:: python

    def print(text):
        sys.stdout.write(text)

.. code-cell:: python
    :execution-count: 1

    def print(text):
        sys.stdout.write(text)

    print("hello world")

.. output-cell::
    :execution-count: 1

    hello world

**配置属性**

.. confval:: demo
    :type: string
    :default: ``"Hello World"``
    :required: False

.. installation:: sphinx-toolbox
    :pypi:
    :anaconda:
    :conda-channels: domdfcoding,conda-forge
    :github:


.. rtfd-shield::
    :project: sphinx-toolbox

**RTD状态**

.. rtfd-shield::
    :project: jianlide
    :version: latest
    :target: https://jianlide.readthedocs.io/zh/latest/index.html

