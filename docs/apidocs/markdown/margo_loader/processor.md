Module margo_loader.processor
=============================
Process a notebook with margo preamble

Functions
---------

    
`get_preamble(cell)`
:   

    
`get_views(cell_preamble: margo_parser.api.classes.MargoBlock.MargoBlock)`
:   Get the submodules this cell belongs to

    
`preamble_contains_directive(cell_preamble: margo_parser.api.classes.MargoBlock.MargoBlock, directive_list)`
:   

    
`preamble_contains_ignore_cell(cell_preamble: margo_parser.api.classes.MargoBlock.MargoBlock)`
:   Determine if a cell contains ignore-cell margo directive

    
`preamble_contains_not_a_module(cell_preamble: margo_parser.api.classes.MargoBlock.MargoBlock)`
:   Determine if a notebook declares that it is not to be imported
    by using the 'not-a-module' directive

    
`preamble_contains_start_module(cell_preamble: margo_parser.api.classes.MargoBlock.MargoBlock)`
:   Determine if a cell contains a start-module subcommand

    
`preamble_contains_stop_module(cell_preamble: margo_parser.api.classes.MargoBlock.MargoBlock)`
:   Determine if a cell contains a stop-module subcommand

    
`remove_magics(source: str) ‑> str`
:   Remove magics from source for execution outside of Jupyter

Classes
-------

`Processor(module, name)`
:   

    ### Methods

    `process_cells(self, cells)`
    :   Parse preambles and execute code cells of a notebook accordingly
        Currently supports:
        # :: ignore-cell :: to skip this cell
        # :: submodule: 'submodule_name' :: to create a virtual submodule in
        which this cell's code will be executed and can later be imported with
        from notebook.submodule_name import stuff_you_defined
        
        If first cell is markdown, it will be used as the module's docstring