About Terminal:
-> Text based interface that lets you interact directly with our os by typing commands

Flow:
1. Type the commands and hit Enter.
2. Shell parses your input and searches path for executable.
3. OS runs the program.
4. The shell prints the resulting text output back to you screen.

Why Terminals?
-> With Terminals, essential for scripting, automating data pipelines, interacting with remote cloud servers, and using tools (like Git or build scripts) that do not have robust graphical interfaces. 
-> Without it, automating repetitive OS-level tasks would be nearly impossible.

How will i know it's working?
-> Type the commands in the cmd like pwd, cd, ls -la, the systems immediately returns the expected output without throwing errors.

Executed commands:

1. pwd command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ pwd
/c/Saturam/saturam-agent-framework

-> Shows your current folder path.


2. ls command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ ls -la
total 164
drwxr-xr-x 1 SMS 197121     0 Nov  5 00:26 ./
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:41 ../
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:42 .claude/
-rw-r--r-- 1 SMS 197121  4717 Oct 22 09:42 .cursorrules
-rw-r--r-- 1 SMS 197121   546 Oct 22 09:42 .dockerignore
-rw-r--r-- 1 SMS 197121   183 Oct 22 09:42 .editorconfig
drwxr-xr-x 1 SMS 197121     0 Nov  2 13:10 .git/
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:42 .github/
-rw-r--r-- 1 SMS 197121  2947 Oct 22 09:42 .gitignore
drwxr-xr-x 1 SMS 197121     0 Nov  4 23:48 .venv/
-rw-r--r-- 1 SMS 197121  7443 Oct 22 09:42 AGENTS.md
-rw-r--r-- 1 SMS 197121 20924 Oct 22 09:42 ARCHITECTURE.md
-rw-r--r-- 1 SMS 197121 12881 Oct 22 09:42 CLAUDE.md
-rw-r--r-- 1 SMS 197121    74 Oct 22 09:42 CODEOWNERS
-rw-r--r-- 1 SMS 197121  5352 Oct 22 09:42 CODE_OF_CONDUCT.md
-rw-r--r-- 1 SMS 197121 16134 Oct 22 09:42 CONTRIBUTING.md
-rw-r--r-- 1 SMS 197121 11543 Oct 22 09:42 LICENSE
-rw-r--r-- 1 SMS 197121   376 Oct 22 09:42 PROVENANCE.md
-rw-r--r-- 1 SMS 197121  3175 Oct 22 09:42 README.md
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:42 benchmarks/
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:42 cookbook/
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:42 deploy/
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:42 docs/
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:42 examples/
drwxr-xr-x 1 SMS 197121     0 Oct 26 12:27 frontend/
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:42 libs/
drwxr-xr-x 1 SMS 197121     0 Nov  4 23:48 product/
-rw-r--r-- 1 SMS 197121   686 Nov  5 00:26 requirements.txt
drwxr-xr-x 1 SMS 197121     0 Oct 22 09:42 scripts/

-> Lists all files (including hidden) with detailed permissions and sizes.

3. cd command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ cd scripts/
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework/scripts (main)

-> Changes directories.

4. head command 
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework/scripts (main)
$ head -n 10 dev_setup.sh
#!/bin/bash

############################################################################
#
#    EGPT Development Setup
#
#    Creates .venv with egptctl and egpt installed in editable mode,
#    with everything the core dev loop needs: unit + integration tests,
#    ./scripts/format.sh and ./scripts/validate.sh.
#    Provider-SDK test dependencies live in ./scripts/test_setup.sh.

-> Displays the first few lines of a file.

5. tail command

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework/scripts (main)
$ tail -n 5 dev_setup.sh
echo ""
if [[ -n "$CLIPBOARD_MSG" ]]; then
    echo -e "    ${DIM}${CLIPBOARD_MSG}${NC}"
    echo ""
fi

-> Displays the last few lines of a file.

6. wc commands 

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework/scripts (main)
$ wc -l dev_setup.sh
102 dev_setup.sh

-> Counts the number of lines.

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework/scripts (main)
$ cd ..
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)

7. grep commands 

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ grep -n "export" scripts/dev_setup.sh


(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ grep -c "setup" README.md
2

-> Searches for specific text inside files.

8. find command

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ find . -name "*.md" -type f
./.github/pull_request_template.md
./.venv/Lib/site-packages/datamodel_code_generator/resources/datamodel-code-generator/references/cli-options.md
./.venv/Lib/site-packages/datamodel_code_generator/resources/datamodel-code-generator/references/troubleshooting.md
./.venv/Lib/site-packages/datamodel_code_generator/resources/datamodel-code-generator/references/workflows.md
./.venv/Lib/site-packages/datamodel_code_generator/resources/datamodel-code-generator/SKILL.md
./.venv/Lib/site-packages/ddgs-9.16.1.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/docstring_parser-0.18.0.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/fastapi/.agents/skills/fastapi/references/dependencies.md
./.venv/Lib/site-packages/fastapi/.agents/skills/fastapi/references/other-tools.md
./.venv/Lib/site-packages/fastapi/.agents/skills/fastapi/references/path-operations.md
./.venv/Lib/site-packages/fastapi/.agents/skills/fastapi/references/pydantic.md
./.venv/Lib/site-packages/fastapi/.agents/skills/fastapi/references/responses.md
./.venv/Lib/site-packages/fastapi/.agents/skills/fastapi/references/streaming.md
./.venv/Lib/site-packages/fastapi/.agents/skills/fastapi/SKILL.md
./.venv/Lib/site-packages/fastmcp/contrib/bulk_tool_caller/README.md
./.venv/Lib/site-packages/fastmcp/contrib/component_manager/README.md
./.venv/Lib/site-packages/fastmcp/contrib/mcp_mixin/README.md
./.venv/Lib/site-packages/fastmcp/contrib/README.md
./.venv/Lib/site-packages/fastmcp/server/openapi/README.md
./.venv/Lib/site-packages/fastmcp/utilities/openapi/README.md
./.venv/Lib/site-packages/httpcore-1.0.9.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/httpcore2-2.16.0.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/httpx-0.28.1.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/httpx2-2.16.0.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/idna-3.20.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/markdown-3.11.2.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/mypy/typeshed/stdlib/_typeshed/README.md
./.venv/Lib/site-packages/nltk-3.10.0.dist-info/licenses/AUTHORS.md
./.venv/Lib/site-packages/nltk-3.10.0.dist-info/licenses/README.md
./.venv/Lib/site-packages/numpy/random/LICENSE.md
./.venv/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
./.venv/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/LICENSE.md
./.venv/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
./.venv/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
./.venv/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
./.venv/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/philox/LICENSE.md
./.venv/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
./.venv/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
./.venv/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
./.venv/Lib/site-packages/olefile/doc/API.md
./.venv/Lib/site-packages/olefile/doc/Contribute.md
./.venv/Lib/site-packages/olefile/doc/Home.md
./.venv/Lib/site-packages/olefile/doc/Install.md
./.venv/Lib/site-packages/olefile/doc/License.md
./.venv/Lib/site-packages/olefile/doc/OLE_Overview.md
./.venv/Lib/site-packages/openai/lib/live/README.md
./.venv/Lib/site-packages/openai/lib/responses_websocket/README.md
./.venv/Lib/site-packages/openai/resources/conversations/api.md
./.venv/Lib/site-packages/openai/resources/live/api.md
./.venv/Lib/site-packages/openai/resources/realtime/api.md
./.venv/Lib/site-packages/openai/resources/responses/api.md
./.venv/Lib/site-packages/openai/resources/webhooks/api.md
./.venv/Lib/site-packages/openai/_vendor/httpx_aiohttp/FORK.md
./.venv/Lib/site-packages/openai/_vendor/httpx_aiohttp/README.md
./.venv/Lib/site-packages/openapi_pydantic/v3/v3_0/README.md
./.venv/Lib/site-packages/openapi_pydantic/v3/v3_1/README.md
./.venv/Lib/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.md
./.venv/Lib/site-packages/pypdfium2-5.14.0.dist-info/licenses/data/windows_x64/BUILD_LICENSES/libjpeg_turbo.md
./.venv/Lib/site-packages/soupsieve-4.0.1.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/starlette-1.10.0.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/typer/.agents/skills/typer/SKILL.md
./.venv/Lib/site-packages/unstructured-0.18.27.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/unstructured_client-0.46.4.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/uvicorn-0.54.0.dist-info/licenses/LICENSE.md
./.venv/Lib/site-packages/win32comext/mapi/NOTICE.md
./AGENTS.md
./ARCHITECTURE.md
./benchmarks/memory_bitemporal/findings/phase1_foundation.md
./benchmarks/memory_bitemporal/README.md
./benchmarks/memory_bitemporal/results/summary_20260723T162455Z.md
./benchmarks/memory_bitemporal/results/summary_20260729T061116Z.md
./benchmarks/memory_bitemporal/SPEC.md
./benchmarks/memory_bitemporal/TEST_LOG.md
./benchmarks/memory_consolidation/findings/notes-for-SM-L7.md
./benchmarks/memory_consolidation/README.md
./benchmarks/memory_consolidation/RESEARCH.md
./benchmarks/memory_consolidation/TEST_LOG.md
./benchmarks/memory_datamodel/ddl/MIGRATION.md
./benchmarks/memory_datamodel/findings/README.md
./benchmarks/memory_datamodel/README.md
./benchmarks/memory_datamodel/SPEC.md
./benchmarks/memory_datamodel/TEST_LOG.md
./benchmarks/memory_decay/DECISION.md
./benchmarks/memory_decay/findings/implementation-notes.md
./benchmarks/memory_decay/README.md
./benchmarks/memory_decay/results/ablations.md
./benchmarks/memory_decay/results/confound.md
./benchmarks/memory_decay/results/sensitivity.md
./benchmarks/memory_decay/results/significance.md
./benchmarks/memory_decay/results/significance_embedding.md
./benchmarks/memory_decay/results/summary.md
./benchmarks/memory_decay/results/summary_embedding.md
./benchmarks/memory_decay/TEST_LOG.md
./benchmarks/memory_embedding/DECISION.md
./benchmarks/memory_embedding/findings/README.md
./benchmarks/memory_embedding/README.md
./benchmarks/memory_embedding/TEST_LOG.md
./benchmarks/memory_eval/findings/01-data-quality-and-licensing.md
./benchmarks/memory_eval/findings/02-embedder-coverage-gap.md
./benchmarks/memory_eval/findings/03-graph-multihop-track.md
./benchmarks/memory_eval/PLAN.md
./benchmarks/memory_eval/README.md
./benchmarks/memory_eval/results/summary_20260810T093030Z_fixture_ref.md
./benchmarks/memory_eval/results/summary_20260810T093030Z_fixture_smoke.md
./benchmarks/memory_eval/TEST_LOG.md
./benchmarks/memory_event_segmentation/DECISION.md
./benchmarks/memory_event_segmentation/findings/README.md
./benchmarks/memory_event_segmentation/README.md
./benchmarks/memory_event_segmentation/results/robustness.md
./benchmarks/memory_event_segmentation/results/sensitivity.md
./benchmarks/memory_event_segmentation/results/summary.md
./benchmarks/memory_event_segmentation/results/summary_embedding_llm.md
./benchmarks/memory_event_segmentation/results/summary_embedding_slm.md
./benchmarks/memory_event_segmentation/results/summary_hard.md
./benchmarks/memory_event_segmentation/results/summary_hard_embedding_llm.md
./benchmarks/memory_event_segmentation/results/summary_tiage_llm.md
./benchmarks/memory_event_segmentation/TEST_LOG.md
./benchmarks/memory_graph_engine/README.md
./benchmarks/memory_graph_engine/SPIKE.md
./benchmarks/memory_graph_engine/TEST_LOG.md
./benchmarks/memory_multihop/findings/README.md
./benchmarks/memory_multihop/README.md
./benchmarks/memory_multihop/results/summary_full30.md
./benchmarks/memory_multihop/results/summary_fusion.md
./benchmarks/memory_multihop/results/summary_measurements.md
./benchmarks/memory_multihop/results/summary_smR4ModeA.md
./benchmarks/memory_multihop/SPIKE.md
./benchmarks/memory_multihop/TEST_LOG.md
./benchmarks/memory_provider_spec/findings/README.md
./benchmarks/memory_provider_spec/README.md
./benchmarks/memory_provider_spec/SPEC.md
./benchmarks/memory_provider_spec/TEST_LOG.md
./benchmarks/memory_retrieval/DECISION.md
./benchmarks/memory_retrieval/findings/embedding-async-batch-hang.md
./benchmarks/memory_retrieval/findings/reranker-st-version-seam.md
./benchmarks/memory_retrieval/README.md
./benchmarks/memory_retrieval/results/summary_20260723T112444Z_matrixLocal.md
./benchmarks/memory_retrieval/results/summary_20260723T122020Z_fiqaFusion.md
./benchmarks/memory_retrieval/results/summary_20260728T084006Z_smR4EmbedderVerify.md
./benchmarks/memory_retrieval/results/summary_20260728T090818Z_smR4EmbedderVerifyLME.md
./benchmarks/memory_retrieval/results/sweeps_20260723T112258Z.md
./benchmarks/memory_retrieval/TEST_LOG.md
./benchmarks/memory_vectordb/DECISION.md
./benchmarks/memory_vectordb/EF_SWEEP.md
./benchmarks/memory_vectordb/findings/README.md
./benchmarks/memory_vectordb/README.md
./benchmarks/memory_vectordb/results/summary_20260720T200715Z_matrixA.md
./benchmarks/memory_vectordb/results/summary_20260721T021033Z_matrixB.md
./benchmarks/memory_vectordb/TEST_LOG.md
./CLAUDE.md
./CODE_OF_CONDUCT.md
./CONTRIBUTING.md
./cookbook/00_quickstart/README.md
./cookbook/00_quickstart/TEST_LOG.md
./cookbook/01_demo/README.md
./cookbook/01_demo/TEST_LOG.md
./cookbook/02_agents/01_quickstart/README.md
./cookbook/02_agents/01_quickstart/TEST_LOG.md
./cookbook/02_agents/02_input_output/README.md
./cookbook/02_agents/02_input_output/TEST_LOG.md
./cookbook/02_agents/03_context_management/README.md
./cookbook/02_agents/03_context_management/TEST_LOG.md
./cookbook/02_agents/04_tools/README.md
./cookbook/02_agents/04_tools/TEST_LOG.md
./cookbook/02_agents/05_state_and_session/README.md
./cookbook/02_agents/05_state_and_session/TEST_LOG.md
./cookbook/02_agents/06_memory_and_learning/README.md
./cookbook/02_agents/06_memory_and_learning/TEST_LOG.md
./cookbook/02_agents/07_knowledge/README.md
./cookbook/02_agents/07_knowledge/TEST_LOG.md
./cookbook/02_agents/08_guardrails/README.md
./cookbook/02_agents/08_guardrails/TEST_LOG.md
./cookbook/02_agents/09_hooks/README.md
./cookbook/02_agents/09_hooks/TEST_LOG.md
./cookbook/02_agents/10_human_in_the_loop/README.md
./cookbook/02_agents/10_human_in_the_loop/TEST_LOG.md
./cookbook/02_agents/11_approvals/README.md
./cookbook/02_agents/11_approvals/TEST_LOG.md
./cookbook/02_agents/12_multimodal/README.md
./cookbook/02_agents/12_multimodal/TEST_LOG.md
./cookbook/02_agents/13_reasoning/README.md
./cookbook/02_agents/13_reasoning/TEST_LOG.md
./cookbook/02_agents/14_advanced/interchange_model/README.md
./cookbook/02_agents/14_advanced/README.md
./cookbook/02_agents/14_advanced/TEST_LOG.md
./cookbook/02_agents/15_dependencies/README.md
./cookbook/02_agents/15_dependencies/TEST_LOG.md
./cookbook/02_agents/16_skills/README.md
./cookbook/02_agents/16_skills/sample_skills/code-review/references/style-guide.md
./cookbook/02_agents/16_skills/sample_skills/code-review/SKILL.md
./cookbook/02_agents/16_skills/sample_skills/git-workflow/references/commit-types.md
./cookbook/02_agents/16_skills/sample_skills/git-workflow/SKILL.md
./cookbook/02_agents/16_skills/TEST_LOG.md
./cookbook/02_agents/18_checkpointing/README.md
./cookbook/02_agents/18_checkpointing/TEST_LOG.md
./cookbook/02_agents/19_regenerate/README.md
./cookbook/02_agents/19_regenerate/TEST_LOG.md
./cookbook/02_agents/20_time_travel/README.md
./cookbook/02_agents/20_time_travel/TEST_LOG.md
./cookbook/02_agents/21_fork_session/README.md
./cookbook/02_agents/21_fork_session/TEST_LOG.md
./cookbook/02_agents/README.md
./cookbook/02_agents/TEST_PROMPT.md
./cookbook/03_teams/01_quickstart/README.md
./cookbook/03_teams/01_quickstart/TEST_LOG.md
./cookbook/03_teams/02_modes/broadcast/README.md
./cookbook/03_teams/02_modes/broadcast/TEST_LOG.md
./cookbook/03_teams/02_modes/coordinate/README.md
./cookbook/03_teams/02_modes/coordinate/TEST_LOG.md
./cookbook/03_teams/02_modes/README.md
./cookbook/03_teams/02_modes/route/README.md
./cookbook/03_teams/02_modes/route/TEST_LOG.md
./cookbook/03_teams/02_modes/tasks/README.md
./cookbook/03_teams/02_modes/tasks/TEST_LOG.md
./cookbook/03_teams/02_modes/TEST_LOG.md
./cookbook/03_teams/03_tools/README.md
./cookbook/03_teams/03_tools/TEST_LOG.md
./cookbook/03_teams/04_structured_input_output/README.md
./cookbook/03_teams/04_structured_input_output/TEST_LOG.md
./cookbook/03_teams/05_knowledge/README.md
./cookbook/03_teams/05_knowledge/TEST_LOG.md
./cookbook/03_teams/06_memory/README.md
./cookbook/03_teams/06_memory/TEST_LOG.md
./cookbook/03_teams/07_session/README.md
./cookbook/03_teams/07_session/TEST_LOG.md
./cookbook/03_teams/08_streaming/README.md
./cookbook/03_teams/08_streaming/TEST_LOG.md
./cookbook/03_teams/09_context_management/README.md
./cookbook/03_teams/09_context_management/TEST_LOG.md
./cookbook/03_teams/10_context_compression/README.md
./cookbook/03_teams/10_context_compression/TEST_LOG.md
./cookbook/03_teams/11_reasoning/README.md
./cookbook/03_teams/11_reasoning/TEST_LOG.md
./cookbook/03_teams/12_learning/README.md
./cookbook/03_teams/12_learning/TEST_LOG.md
./cookbook/03_teams/13_hooks/README.md
./cookbook/03_teams/13_hooks/TEST_LOG.md
./cookbook/03_teams/14_run_control/README.md
./cookbook/03_teams/14_run_control/TEST_LOG.md
./cookbook/03_teams/15_distributed_rag/README.md
./cookbook/03_teams/15_distributed_rag/TEST_LOG.md
./cookbook/03_teams/16_search_coordination/README.md
./cookbook/03_teams/16_search_coordination/TEST_LOG.md
./cookbook/03_teams/17_dependencies/README.md
./cookbook/03_teams/17_dependencies/TEST_LOG.md
./cookbook/03_teams/18_guardrails/README.md
./cookbook/03_teams/18_guardrails/TEST_LOG.md
./cookbook/03_teams/19_multimodal/README.md
./cookbook/03_teams/19_multimodal/TEST_LOG.md
./cookbook/03_teams/20_human_in_the_loop/CLAUDE.md
./cookbook/03_teams/20_human_in_the_loop/README.md
./cookbook/03_teams/20_human_in_the_loop/TEST_LOG.md
./cookbook/03_teams/21_state/README.md
./cookbook/03_teams/21_state/TEST_LOG.md
./cookbook/03_teams/22_metrics/README.md
./cookbook/03_teams/22_metrics/TEST_LOG.md
./cookbook/03_teams/23_checkpointing/README.md
./cookbook/03_teams/23_checkpointing/TEST_LOG.md
./cookbook/03_teams/23_remote_agents/README.md
./cookbook/03_teams/24_regenerate/README.md
./cookbook/03_teams/24_regenerate/TEST_LOG.md
./cookbook/03_teams/25_time_travel/README.md
./cookbook/03_teams/25_time_travel/TEST_LOG.md
./cookbook/03_teams/26_fork_session/README.md
./cookbook/03_teams/26_fork_session/TEST_LOG.md
./cookbook/03_teams/README.md
./cookbook/03_teams/TEST_LOG.md
./cookbook/03_teams/TEST_PROMPT.md
./cookbook/04_workflows/01_basic_workflows/01_sequence_of_steps/README.md
./cookbook/04_workflows/01_basic_workflows/01_sequence_of_steps/TEST_LOG.md
./cookbook/04_workflows/01_basic_workflows/02_step_with_function/README.md
./cookbook/04_workflows/01_basic_workflows/02_step_with_function/TEST_LOG.md
./cookbook/04_workflows/01_basic_workflows/03_function_workflows/README.md
./cookbook/04_workflows/01_basic_workflows/03_function_workflows/TEST_LOG.md
./cookbook/04_workflows/01_basic_workflows/README.md
./cookbook/04_workflows/01_basic_workflows/TEST_LOG.md
./cookbook/04_workflows/02_conditional_execution/README.md
./cookbook/04_workflows/02_conditional_execution/TEST_LOG.md
./cookbook/04_workflows/03_loop_execution/README.md
./cookbook/04_workflows/03_loop_execution/TEST_LOG.md
./cookbook/04_workflows/04_parallel_execution/README.md
./cookbook/04_workflows/04_parallel_execution/TEST_LOG.md
./cookbook/04_workflows/05_conditional_branching/README.md
./cookbook/04_workflows/05_conditional_branching/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/background_execution/README.md
./cookbook/04_workflows/06_advanced_concepts/background_execution/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/early_stopping/README.md
./cookbook/04_workflows/06_advanced_concepts/early_stopping/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/guardrails/README.md
./cookbook/04_workflows/06_advanced_concepts/guardrails/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/history/README.md
./cookbook/04_workflows/06_advanced_concepts/history/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/long_running/README.md
./cookbook/04_workflows/06_advanced_concepts/long_running/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/previous_step_outputs/README.md
./cookbook/04_workflows/06_advanced_concepts/previous_step_outputs/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/README.md
./cookbook/04_workflows/06_advanced_concepts/run_control/README.md
./cookbook/04_workflows/06_advanced_concepts/run_control/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/run_params/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/session_state/README.md
./cookbook/04_workflows/06_advanced_concepts/session_state/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/structured_io/README.md
./cookbook/04_workflows/06_advanced_concepts/structured_io/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/tools/README.md
./cookbook/04_workflows/06_advanced_concepts/tools/TEST_LOG.md
./cookbook/04_workflows/06_advanced_concepts/workflow_agent/README.md
./cookbook/04_workflows/06_advanced_concepts/workflow_agent/TEST_LOG.md
./cookbook/04_workflows/07_cel_expressions/condition/README.md
./cookbook/04_workflows/07_cel_expressions/condition/TEST_LOG.md
./cookbook/04_workflows/07_cel_expressions/loop/README.md
./cookbook/04_workflows/07_cel_expressions/loop/TEST_LOG.md
./cookbook/04_workflows/07_cel_expressions/README.md
./cookbook/04_workflows/07_cel_expressions/router/README.md
./cookbook/04_workflows/07_cel_expressions/router/TEST_LOG.md
./cookbook/04_workflows/07_cel_expressions/TEST_LOG.md
./cookbook/04_workflows/assets/TEST_LOG.md
./cookbook/04_workflows/README.md
./cookbook/04_workflows/TEST_LOG.md
./cookbook/04_workflows/TEST_PROMPT.md
./cookbook/05_agent_os/advanced_demo/README.md
./cookbook/05_agent_os/advanced_demo/TEST_LOG.md
./cookbook/05_agent_os/background_tasks/README.md
./cookbook/05_agent_os/background_tasks/TEST_LOG.md
./cookbook/05_agent_os/client/README.md
./cookbook/05_agent_os/client/TEST_LOG.md
./cookbook/05_agent_os/client_a2a/README.md
./cookbook/05_agent_os/client_a2a/servers/README.md
./cookbook/05_agent_os/client_a2a/servers/TEST_LOG.md
./cookbook/05_agent_os/client_a2a/TEST_LOG.md
./cookbook/05_agent_os/customize/README.md
./cookbook/05_agent_os/customize/TEST_LOG.md
./cookbook/05_agent_os/dbs/README.md
./cookbook/05_agent_os/dbs/surreal_db/README.md
./cookbook/05_agent_os/dbs/surreal_db/TEST_LOG.md
./cookbook/05_agent_os/dbs/TEST_LOG.md
./cookbook/05_agent_os/factories/README.md
./cookbook/05_agent_os/factories/TEST_LOG.md
./cookbook/05_agent_os/human_in_the_loop/README.md
./cookbook/05_agent_os/integrations/README.md
./cookbook/05_agent_os/integrations/TEST_LOG.md
./cookbook/05_agent_os/interfaces/a2a/basic_agent/README.md
./cookbook/05_agent_os/interfaces/a2a/basic_agent/TEST_LOG.md
./cookbook/05_agent_os/interfaces/a2a/multi_agent_a2a/README.md
./cookbook/05_agent_os/interfaces/a2a/multi_agent_a2a/TEST_LOG.md
./cookbook/05_agent_os/interfaces/a2a/README.md
./cookbook/05_agent_os/interfaces/a2a/TEST_LOG.md
./cookbook/05_agent_os/interfaces/agui/README.md
./cookbook/05_agent_os/interfaces/agui/TEST_LOG.md
./cookbook/05_agent_os/interfaces/discord/README.md
./cookbook/05_agent_os/interfaces/discord/TEST_LOG.md
./cookbook/05_agent_os/interfaces/README.md
./cookbook/05_agent_os/interfaces/slack/README.md
./cookbook/05_agent_os/interfaces/slack/TEST_LOG.md
./cookbook/05_agent_os/interfaces/telegram/README.md
./cookbook/05_agent_os/interfaces/TEST_LOG.md
./cookbook/05_agent_os/interfaces/whatsapp/README.md
./cookbook/05_agent_os/interfaces/whatsapp/TEST_LOG.md
./cookbook/05_agent_os/knowledge/README.md
./cookbook/05_agent_os/knowledge/TEST_LOG.md
./cookbook/05_agent_os/learnings/README.md
./cookbook/05_agent_os/learnings/TEST_LOG.md
./cookbook/05_agent_os/mcp_demo/dynamic_headers/README.md
./cookbook/05_agent_os/mcp_demo/dynamic_headers/TEST_LOG.md
./cookbook/05_agent_os/mcp_demo/README.md
./cookbook/05_agent_os/mcp_demo/TEST_LOG.md
./cookbook/05_agent_os/middleware/README.md
./cookbook/05_agent_os/middleware/TEST_LOG.md
./cookbook/05_agent_os/os_config/README.md
./cookbook/05_agent_os/os_config/TEST_LOG.md
./cookbook/05_agent_os/rbac/asymmetric/README.md
./cookbook/05_agent_os/rbac/asymmetric/TEST_LOG.md
./cookbook/05_agent_os/rbac/README.md
./cookbook/05_agent_os/rbac/symmetric/README.md
./cookbook/05_agent_os/rbac/symmetric/TEST_LOG.md
./cookbook/05_agent_os/README.md
./cookbook/05_agent_os/remote/README.md
./cookbook/05_agent_os/remote/TEST_LOG.md
./cookbook/05_agent_os/scheduler/CLAUDE.md
./cookbook/05_agent_os/scheduler/README.md
./cookbook/05_agent_os/scheduler/TEST_LOG.md
./cookbook/05_agent_os/schemas/README.md
./cookbook/05_agent_os/schemas/TEST_LOG.md
./cookbook/05_agent_os/skills/README.md
./cookbook/05_agent_os/skills/sample_skills/system-info/scripts/README.md
./cookbook/05_agent_os/skills/sample_skills/system-info/scripts/TEST_LOG.md
./cookbook/05_agent_os/skills/sample_skills/system-info/SKILL.md
./cookbook/05_agent_os/skills/TEST_LOG.md
./cookbook/05_agent_os/studio_tool/README.md
./cookbook/05_agent_os/studio_tool/TEST_LOG.md
./cookbook/05_agent_os/TEST_LOG.md
./cookbook/05_agent_os/TEST_PROMPT.md
./cookbook/05_agent_os/tracing/dbs/README.md
./cookbook/05_agent_os/tracing/dbs/TEST_LOG.md
./cookbook/05_agent_os/tracing/README.md
./cookbook/05_agent_os/tracing/TEST_LOG.md
./cookbook/05_agent_os/workflow/README.md
./cookbook/05_agent_os/workflow/TEST_LOG.md
./cookbook/06_storage/dynamodb/README.md
./cookbook/06_storage/dynamodb/TEST_LOG.md
./cookbook/06_storage/examples/README.md
./cookbook/06_storage/examples/TEST_LOG.md
./cookbook/06_storage/firestore/README.md
./cookbook/06_storage/firestore/TEST_LOG.md
./cookbook/06_storage/gcs/README.md
./cookbook/06_storage/gcs/TEST_LOG.md
./cookbook/06_storage/in_memory/README.md
./cookbook/06_storage/in_memory/TEST_LOG.md
./cookbook/06_storage/json_db/README.md
./cookbook/06_storage/json_db/TEST_LOG.md
./cookbook/06_storage/mongo/async_mongo/README.md
./cookbook/06_storage/mongo/async_mongo/TEST_LOG.md
./cookbook/06_storage/mongo/README.md
./cookbook/06_storage/mongo/TEST_LOG.md
./cookbook/06_storage/mysql/async_mysql/README.md
./cookbook/06_storage/mysql/async_mysql/TEST_LOG.md
./cookbook/06_storage/mysql/README.md
./cookbook/06_storage/mysql/TEST_LOG.md
./cookbook/06_storage/postgres/async_postgres/README.md
./cookbook/06_storage/postgres/async_postgres/TEST_LOG.md
./cookbook/06_storage/postgres/README.md
./cookbook/06_storage/postgres/TEST_LOG.md
./cookbook/06_storage/README.md
./cookbook/06_storage/redis/README.md
./cookbook/06_storage/redis/TEST_LOG.md
./cookbook/06_storage/singlestore/README.md
./cookbook/06_storage/singlestore/TEST_LOG.md
./cookbook/06_storage/sqlite/async_sqlite/README.md
./cookbook/06_storage/sqlite/async_sqlite/TEST_LOG.md
./cookbook/06_storage/sqlite/README.md
./cookbook/06_storage/sqlite/TEST_LOG.md
./cookbook/06_storage/surrealdb/README.md
./cookbook/06_storage/surrealdb/TEST_LOG.md
./cookbook/06_storage/TEST_LOG.md
./cookbook/06_storage/TEST_PROMPT.md
./cookbook/07_knowledge/01_getting_started/README.md
./cookbook/07_knowledge/02_building_blocks/README.md
./cookbook/07_knowledge/03_production/README.md
./cookbook/07_knowledge/04_advanced/README.md
./cookbook/07_knowledge/05_integrations/rag/README.md
./cookbook/07_knowledge/05_integrations/rag/TEST_LOG.md
./cookbook/07_knowledge/05_integrations/README.md
./cookbook/07_knowledge/09_archive/README.md
./cookbook/07_knowledge/README.md
./cookbook/07_knowledge/testing_resources/coffee.md
./cookbook/07_knowledge/testing_resources/README.md
./cookbook/07_knowledge/TEST_LOG.md
./cookbook/07_knowledge/TEST_PROMPT.md
./cookbook/08_learning/00_quickstart/README.md
./cookbook/08_learning/00_quickstart/TEST_LOG.md
./cookbook/08_learning/01_basics/README.md
./cookbook/08_learning/01_basics/TEST_LOG.md
./cookbook/08_learning/02_user_profile/README.md
./cookbook/08_learning/02_user_profile/TEST_LOG.md
./cookbook/08_learning/03_session_context/README.md
./cookbook/08_learning/03_session_context/TEST_LOG.md
./cookbook/08_learning/04_entity_memory/README.md
./cookbook/08_learning/04_entity_memory/TEST_LOG.md
./cookbook/08_learning/05_learned_knowledge/README.md
./cookbook/08_learning/05_learned_knowledge/TEST_LOG.md
./cookbook/08_learning/06_quick_tests/README.md
./cookbook/08_learning/06_quick_tests/TEST_LOG.md
./cookbook/08_learning/07_patterns/README.md
./cookbook/08_learning/07_patterns/TEST_LOG.md
./cookbook/08_learning/08_custom_stores/README.md
./cookbook/08_learning/08_custom_stores/TEST_LOG.md
./cookbook/08_learning/09_decision_logs/README.md
./cookbook/08_learning/09_decision_logs/TEST_LOG.md
./cookbook/08_learning/10_demo/README.md
./cookbook/08_learning/10_demo/TEST_LOG.md
./cookbook/08_learning/README.md
./cookbook/08_learning/TEST_LOG.md
./cookbook/08_learning/TEST_PROMPT.md
./cookbook/09_evals/accuracy/README.md
./cookbook/09_evals/accuracy/TEST_LOG.md
./cookbook/09_evals/agent_as_judge/README.md
./cookbook/09_evals/agent_as_judge/TEST_LOG.md
./cookbook/09_evals/performance/comparison/README.md
./cookbook/09_evals/performance/comparison/TEST_LOG.md
./cookbook/09_evals/performance/README.md
./cookbook/09_evals/performance/TEST_LOG.md
./cookbook/09_evals/README.md
./cookbook/09_evals/reliability/multiple_tool_calls/README.md
./cookbook/09_evals/reliability/multiple_tool_calls/TEST_LOG.md
./cookbook/09_evals/reliability/README.md
./cookbook/09_evals/reliability/single_tool_calls/README.md
./cookbook/09_evals/reliability/single_tool_calls/TEST_LOG.md
./cookbook/09_evals/reliability/team/README.md
./cookbook/09_evals/reliability/team/TEST_LOG.md
./cookbook/09_evals/reliability/TEST_LOG.md
./cookbook/09_evals/suite/README.md
./cookbook/09_evals/suite/TEST_LOG.md
./cookbook/09_evals/TEST_LOG.md
./cookbook/09_evals/TEST_PROMPT.md
./cookbook/10_reasoning/agents/README.md
./cookbook/10_reasoning/agents/TEST_LOG.md
./cookbook/10_reasoning/models/anthropic/README.md
./cookbook/10_reasoning/models/anthropic/TEST_LOG.md
./cookbook/10_reasoning/models/azure_ai_foundry/README.md
./cookbook/10_reasoning/models/azure_ai_foundry/TEST_LOG.md
./cookbook/10_reasoning/models/azure_openai/README.md
./cookbook/10_reasoning/models/azure_openai/TEST_LOG.md
./cookbook/10_reasoning/models/deepseek/README.md
./cookbook/10_reasoning/models/deepseek/TEST_LOG.md
./cookbook/10_reasoning/models/gemini/README.md
./cookbook/10_reasoning/models/gemini/TEST_LOG.md
./cookbook/10_reasoning/models/groq/README.md
./cookbook/10_reasoning/models/groq/TEST_LOG.md
./cookbook/10_reasoning/models/ollama/README.md
./cookbook/10_reasoning/models/ollama/TEST_LOG.md
./cookbook/10_reasoning/models/openai/README.md
./cookbook/10_reasoning/models/openai/TEST_LOG.md
./cookbook/10_reasoning/models/README.md
./cookbook/10_reasoning/models/TEST_LOG.md
./cookbook/10_reasoning/models/vertex_ai/README.md
./cookbook/10_reasoning/models/vertex_ai/TEST_LOG.md
./cookbook/10_reasoning/models/xai/README.md
./cookbook/10_reasoning/models/xai/TEST_LOG.md
./cookbook/10_reasoning/README.md
./cookbook/10_reasoning/teams/README.md
./cookbook/10_reasoning/teams/TEST_LOG.md
./cookbook/10_reasoning/TEST_LOG.md
./cookbook/10_reasoning/TEST_PROMPT.md
./cookbook/10_reasoning/tools/README.md
./cookbook/10_reasoning/tools/TEST_LOG.md
./cookbook/11_memory/integrations/README.md
./cookbook/11_memory/integrations/TEST_LOG.md
./cookbook/11_memory/memory_manager/README.md
./cookbook/11_memory/memory_manager/TEST_LOG.md
./cookbook/11_memory/optimize_memories/README.md
./cookbook/11_memory/optimize_memories/TEST_LOG.md
./cookbook/11_memory/README.md
./cookbook/11_memory/TEST_LOG.md
./cookbook/11_memory/TEST_PROMPT.md
./cookbook/12_context/README.md
./cookbook/12_context/TEST_LOG.md
./cookbook/90_models/aimlapi/README.md
./cookbook/90_models/aimlapi/TEST_LOG.md
./cookbook/90_models/anthropic/README.md
./cookbook/90_models/anthropic/skills/README.md
./cookbook/90_models/anthropic/skills/TEST_LOG.md
./cookbook/90_models/anthropic/TEST_LOG.md
./cookbook/90_models/aws/bedrock/README.md
./cookbook/90_models/aws/bedrock/TEST_LOG.md
./cookbook/90_models/aws/claude/README.md
./cookbook/90_models/aws/claude/TEST_LOG.md
./cookbook/90_models/aws/README.md
./cookbook/90_models/aws/TEST_LOG.md
./cookbook/90_models/azure/ai_foundry/README.md
./cookbook/90_models/azure/ai_foundry/TEST_LOG.md
./cookbook/90_models/azure/claude/README.md
./cookbook/90_models/azure/openai/README.md
./cookbook/90_models/azure/openai/TEST_LOG.md
./cookbook/90_models/azure/README.md
./cookbook/90_models/azure/TEST_LOG.md
./cookbook/90_models/cerebras/README.md
./cookbook/90_models/cerebras/TEST_LOG.md
./cookbook/90_models/cerebras_openai/README.md
./cookbook/90_models/cerebras_openai/TEST_LOG.md
./cookbook/90_models/clients/README.md
./cookbook/90_models/clients/TEST_LOG.md
./cookbook/90_models/cloudflare/README.md
./cookbook/90_models/cloudflare/TEST_LOG.md
./cookbook/90_models/cohere/README.md
./cookbook/90_models/cohere/TEST_LOG.md
./cookbook/90_models/cometapi/README.md
./cookbook/90_models/cometapi/TEST_LOG.md
./cookbook/90_models/dashscope/README.md
./cookbook/90_models/dashscope/TEST_LOG.md
./cookbook/90_models/deepinfra/README.md
./cookbook/90_models/deepinfra/TEST_LOG.md
./cookbook/90_models/deepseek/README.md
./cookbook/90_models/deepseek/TEST_LOG.md
./cookbook/90_models/fireworks/README.md
./cookbook/90_models/fireworks/TEST_LOG.md
./cookbook/90_models/google/gemini/documents/readme.md
./cookbook/90_models/google/gemini/documents/TEST_LOG.md
./cookbook/90_models/google/gemini/README.md
./cookbook/90_models/google/gemini/TEST_LOG.md
./cookbook/90_models/google/gemini_interactions/README.md
./cookbook/90_models/google/gemini_interactions/TEST_LOG.md
./cookbook/90_models/google/README.md
./cookbook/90_models/google/TEST_LOG.md
./cookbook/90_models/groq/README.md
./cookbook/90_models/groq/reasoning/README.md
./cookbook/90_models/groq/reasoning/TEST_LOG.md
./cookbook/90_models/groq/TEST_LOG.md
./cookbook/90_models/huggingface/README.md
./cookbook/90_models/huggingface/TEST_LOG.md
./cookbook/90_models/ibm/README.md
./cookbook/90_models/ibm/TEST_LOG.md
./cookbook/90_models/ibm/watsonx/README.md
./cookbook/90_models/ibm/watsonx/TEST_LOG.md
./cookbook/90_models/inception/README.md
./cookbook/90_models/inception/TEST_LOG.md
./cookbook/90_models/internlm/README.md
./cookbook/90_models/internlm/TEST_LOG.md
./cookbook/90_models/langdb/README.md
./cookbook/90_models/langdb/TEST_LOG.md
./cookbook/90_models/litellm/README.md
./cookbook/90_models/litellm/TEST_LOG.md
./cookbook/90_models/litellm_openai/README.md
./cookbook/90_models/litellm_openai/TEST_LOG.md
./cookbook/90_models/llama_cpp/README.md
./cookbook/90_models/llama_cpp/TEST_LOG.md
./cookbook/90_models/lmstudio/README.md
./cookbook/90_models/lmstudio/TEST_LOG.md
./cookbook/90_models/meta/llama/README.md
./cookbook/90_models/meta/llama/TEST_LOG.md
./cookbook/90_models/meta/llama_openai/README.md
./cookbook/90_models/meta/llama_openai/TEST_LOG.md
./cookbook/90_models/meta/README.md
./cookbook/90_models/meta/TEST_LOG.md
./cookbook/90_models/minimax/README.md
./cookbook/90_models/minimax/TEST_LOG.md
./cookbook/90_models/mistral/README.md
./cookbook/90_models/mistral/TEST_LOG.md
./cookbook/90_models/moonshot/README.md
./cookbook/90_models/moonshot/TEST_LOG.md
./cookbook/90_models/n1n/README.md
./cookbook/90_models/n1n/TEST_LOG.md
./cookbook/90_models/nebius/README.md
./cookbook/90_models/nebius/TEST_LOG.md
./cookbook/90_models/neosantara/README.md
./cookbook/90_models/neosantara/TEST_LOG.md
./cookbook/90_models/nexus/README.md
./cookbook/90_models/nexus/TEST_LOG.md
./cookbook/90_models/nvidia/README.md
./cookbook/90_models/nvidia/TEST_LOG.md
./cookbook/90_models/ollama/chat/README.md
./cookbook/90_models/ollama/chat/TEST_LOG.md
./cookbook/90_models/ollama/README.md
./cookbook/90_models/ollama/responses/README.md
./cookbook/90_models/ollama/responses/TEST_LOG.md
./cookbook/90_models/ollama/TEST_LOG.md
./cookbook/90_models/openai/chat/README.md
./cookbook/90_models/openai/chat/TEST_LOG.md
./cookbook/90_models/openai/README.md
./cookbook/90_models/openai/responses/README.md
./cookbook/90_models/openai/responses/TEST_LOG.md
./cookbook/90_models/openai/TEST_LOG.md
./cookbook/90_models/openrouter/chat/README.md
./cookbook/90_models/openrouter/chat/TEST_LOG.md
./cookbook/90_models/openrouter/README.md
./cookbook/90_models/openrouter/responses/README.md
./cookbook/90_models/openrouter/responses/TEST_LOG.md
./cookbook/90_models/openrouter/TEST_LOG.md
./cookbook/90_models/perplexity/README.md
./cookbook/90_models/perplexity/TEST_LOG.md
./cookbook/90_models/portkey/README.md
./cookbook/90_models/portkey/TEST_LOG.md
./cookbook/90_models/README.md
./cookbook/90_models/requesty/README.md
./cookbook/90_models/requesty/TEST_LOG.md
./cookbook/90_models/sambanova/README.md
./cookbook/90_models/sambanova/TEST_LOG.md
./cookbook/90_models/siliconflow/README.md
./cookbook/90_models/siliconflow/TEST_LOG.md
./cookbook/90_models/TEST_LOG.md
./cookbook/90_models/TEST_PROMPT.md
./cookbook/90_models/together/README.md
./cookbook/90_models/together/TEST_LOG.md
./cookbook/90_models/tuning_engines/README.md
./cookbook/90_models/vercel/README.md
./cookbook/90_models/vercel/TEST_LOG.md
./cookbook/90_models/vertexai/claude/README.md
./cookbook/90_models/vertexai/claude/TEST_LOG.md
./cookbook/90_models/vertexai/README.md
./cookbook/90_models/vertexai/TEST_LOG.md
./cookbook/90_models/vllm/README.md
./cookbook/90_models/vllm/TEST_LOG.md
./cookbook/90_models/xai/README.md
./cookbook/90_models/xai/TEST_LOG.md
./cookbook/90_models/xiaomi/README.md
./cookbook/90_models/xiaomi/TEST_LOG.md
./cookbook/91_tools/coding_tools/README.md
./cookbook/91_tools/coding_tools/TEST_LOG.md
./cookbook/91_tools/docling_tools/README.md
./cookbook/91_tools/exceptions/README.md
./cookbook/91_tools/exceptions/TEST_LOG.md
./cookbook/91_tools/google/README.md
./cookbook/91_tools/mcp/dynamic_headers/README.md
./cookbook/91_tools/mcp/dynamic_headers/TEST_LOG.md
./cookbook/91_tools/mcp/local_server/README.md
./cookbook/91_tools/mcp/local_server/TEST_LOG.md
./cookbook/91_tools/mcp/mcp_toolbox_demo/README.md
./cookbook/91_tools/mcp/mcp_toolbox_demo/TEST_LOG.md
./cookbook/91_tools/mcp/README.md
./cookbook/91_tools/mcp/sse_transport/README.md
./cookbook/91_tools/mcp/sse_transport/TEST_LOG.md
./cookbook/91_tools/mcp/streamable_http_transport/README.md
./cookbook/91_tools/mcp/streamable_http_transport/TEST_LOG.md
./cookbook/91_tools/mcp/TEST_LOG.md
./cookbook/91_tools/models/README.md
./cookbook/91_tools/models/TEST_LOG.md
./cookbook/91_tools/other/README.md
./cookbook/91_tools/other/TEST_LOG.md
./cookbook/91_tools/parallel/README.md
./cookbook/91_tools/README.md
./cookbook/91_tools/TEST_LOG.md
./cookbook/91_tools/TEST_PROMPT.md
./cookbook/91_tools/tool_decorator/README.md
./cookbook/91_tools/tool_decorator/TEST_LOG.md
./cookbook/91_tools/tool_hooks/README.md
./cookbook/91_tools/tool_hooks/TEST_LOG.md
./cookbook/91_tools/workspace_tools/README.md
./cookbook/91_tools/workspace_tools/TEST_LOG.md
./cookbook/93_components/README.md
./cookbook/93_components/TEST_LOG.md
./cookbook/93_components/TEST_PROMPT.md
./cookbook/93_components/workflows/README.md
./cookbook/93_components/workflows/TEST_LOG.md
./cookbook/94_retail/K08_BASELINE.md
./cookbook/94_retail/K12_BASELINE.md
./cookbook/94_retail/K13_BASELINE.md
./cookbook/94_retail/K15_BASELINE.md
./cookbook/94_retail/R03_prototype_screen.md
./cookbook/94_retail/README.md
./cookbook/94_retail/TEST_LOG.md
./cookbook/95_azure_migration/AZ_B_dimension_and_scoring_decisions.md
./cookbook/95_azure_migration/README.md
./cookbook/95_azure_migration/TEST_LOG.md
./cookbook/data_labeling/image_search/README.md
./cookbook/data_labeling/image_search/TEST_LOG.md
./cookbook/data_labeling/README.md
./cookbook/data_labeling/_01_text_classification/README.md
./cookbook/data_labeling/_01_text_classification/TEST_LOG.md
./cookbook/data_labeling/_02_text_multilabel_classification/README.md
./cookbook/data_labeling/_02_text_multilabel_classification/TEST_LOG.md
./cookbook/data_labeling/_03_text_extraction/README.md
./cookbook/data_labeling/_03_text_extraction/TEST_LOG.md
./cookbook/data_labeling/_04_text_span_labeling/README.md
./cookbook/data_labeling/_04_text_span_labeling/TEST_LOG.md
./cookbook/data_labeling/_05_text_pairwise_preference/README.md
./cookbook/data_labeling/_05_text_pairwise_preference/TEST_LOG.md
./cookbook/data_labeling/_06_image_classification/README.md
./cookbook/data_labeling/_06_image_classification/TEST_LOG.md
./cookbook/data_labeling/_07_image_extraction/README.md
./cookbook/data_labeling/_07_image_extraction/TEST_LOG.md
./cookbook/data_labeling/_08_image_bounding_boxes/README.md
./cookbook/data_labeling/_08_image_bounding_boxes/TEST_LOG.md
./cookbook/data_labeling/_09_image_extraction_to_vectordb/README.md
./cookbook/data_labeling/_09_image_extraction_to_vectordb/TEST_LOG.md
./cookbook/data_labeling/_10_audio_classification/README.md
./cookbook/data_labeling/_10_audio_classification/TEST_LOG.md
./cookbook/data_labeling/_11_audio_transcription/README.md
./cookbook/data_labeling/_11_audio_transcription/TEST_LOG.md
./cookbook/data_labeling/_12_audio_extraction/README.md
./cookbook/data_labeling/_12_audio_extraction/TEST_LOG.md
./cookbook/data_labeling/_13_video_classification/README.md
./cookbook/data_labeling/_13_video_classification/TEST_LOG.md
./cookbook/data_labeling/_14_video_extraction/README.md
./cookbook/data_labeling/_14_video_extraction/TEST_LOG.md
./cookbook/data_labeling/_15_document_classification/README.md
./cookbook/data_labeling/_15_document_classification/TEST_LOG.md
./cookbook/data_labeling/_16_document_extraction/README.md
./cookbook/data_labeling/_16_document_extraction/TEST_LOG.md
./cookbook/data_labeling/_17_llm_as_judge/README.md
./cookbook/data_labeling/_17_llm_as_judge/TEST_LOG.md
./cookbook/data_labeling/_18_quality_review/README.md
./cookbook/data_labeling/_18_quality_review/TEST_LOG.md
./cookbook/frameworks/00_quickstart/README.md
./cookbook/frameworks/antigravity/example_agent/AGENTS.md
./cookbook/frameworks/antigravity/example_agent/skills/haiku/SKILL.md
./cookbook/frameworks/antigravity/README.md
./cookbook/frameworks/antigravity/TEST_LOG.md
./cookbook/gemini_3/README.md
./cookbook/gemini_3/use_cases/README.md
./cookbook/integrations/parallel/README.md
./cookbook/integrations/parallel/TEST_LOG.md
./cookbook/integrations/README.md
./cookbook/integrations/surrealdb/README.md
./cookbook/integrations/surrealdb/TEST_LOG.md
./cookbook/integrations/TEST_LOG.md
./cookbook/integrations/TEST_PROMPT.md
./cookbook/levels_of_agentic_software/README.md
./cookbook/levels_of_agentic_software/TEST_LOG.md
./cookbook/observability/README.md
./cookbook/observability/teams/README.md
./cookbook/observability/teams/TEST_LOG.md
./cookbook/observability/TEST_LOG.md
./cookbook/observability/workflows/README.md
./cookbook/observability/workflows/TEST_LOG.md
./cookbook/README.md
./cookbook/STYLE_GUIDE.md
./deploy/AKS_CUTOVER.md
./deploy/AZURE_CUTOVER.md
./deploy/helm/egpt/README.md
./deploy/README.md
./deploy/vm/README.md
./docs/adr/0001-layered-architecture.md
./docs/adr/0002-dependency-injection.md
./docs/adr/0003-symbiotic-memory.md
./docs/adr/0004-component-tenant-isolation.md
./docs/capability-policy.md
./docs/component-config-schema.md
./docs/component-lifecycle.md
./docs/component-portability.md
./docs/di.md
./docs/integrations-inventory.md
./docs/MEMORY-RESEARCH-episodic-and-neurosymbolic.md
./docs/plan/analytics-automation-design.md
./docs/plan/azure-migration-plan.md
./docs/plan/build-plan.md
./docs/plan/delivery-plan.md
./docs/plan/document-use-case-flow-short.md
./docs/plan/document-use-case-flow.md
./docs/plan/domain-knowledge-layers.md
./docs/plan/open-items.md
./docs/tenancy.md
./frontend/node_modules/@alloc/quick-lru/readme.md
./frontend/node_modules/@babel/code-frame/README.md
./frontend/node_modules/@babel/compat-data/README.md
./frontend/node_modules/@babel/core/README.md
./frontend/node_modules/@babel/generator/README.md
./frontend/node_modules/@babel/helper-compilation-targets/README.md
./frontend/node_modules/@babel/helper-globals/README.md
./frontend/node_modules/@babel/helper-module-imports/README.md
./frontend/node_modules/@babel/helper-module-transforms/README.md
./frontend/node_modules/@babel/helper-plugin-utils/README.md
./frontend/node_modules/@babel/helper-string-parser/README.md
./frontend/node_modules/@babel/helper-validator-identifier/README.md
./frontend/node_modules/@babel/helper-validator-option/README.md
./frontend/node_modules/@babel/helpers/README.md
./frontend/node_modules/@babel/parser/CHANGELOG.md
./frontend/node_modules/@babel/parser/README.md
./frontend/node_modules/@babel/plugin-transform-react-jsx-self/README.md
./frontend/node_modules/@babel/plugin-transform-react-jsx-source/README.md
./frontend/node_modules/@babel/runtime/README.md
./frontend/node_modules/@babel/template/README.md
./frontend/node_modules/@babel/traverse/README.md
./frontend/node_modules/@babel/types/README.md
./frontend/node_modules/@esbuild/win32-x64/README.md
./frontend/node_modules/@jridgewell/gen-mapping/README.md
./frontend/node_modules/@jridgewell/remapping/README.md
./frontend/node_modules/@jridgewell/resolve-uri/README.md
./frontend/node_modules/@jridgewell/sourcemap-codec/README.md
./frontend/node_modules/@jridgewell/trace-mapping/README.md
./frontend/node_modules/@nodelib/fs.scandir/README.md
./frontend/node_modules/@nodelib/fs.stat/README.md
./frontend/node_modules/@nodelib/fs.walk/README.md
./frontend/node_modules/@rollup/rollup-win32-x64-gnu/README.md
./frontend/node_modules/@rollup/rollup-win32-x64-msvc/README.md
./frontend/node_modules/@supabase/auth-js/AGENTS.md
./frontend/node_modules/@supabase/auth-js/migrations/lockless-coordination.md
./frontend/node_modules/@supabase/auth-js/migrations/README.md
./frontend/node_modules/@supabase/auth-js/README.md
./frontend/node_modules/@supabase/functions-js/AGENTS.md
./frontend/node_modules/@supabase/functions-js/migrations/README.md
./frontend/node_modules/@supabase/functions-js/README.md
./frontend/node_modules/@supabase/phoenix/LICENSE.md
./frontend/node_modules/@supabase/phoenix/README.md
./frontend/node_modules/@supabase/postgrest-js/AGENTS.md
./frontend/node_modules/@supabase/postgrest-js/migrations/README.md
./frontend/node_modules/@supabase/postgrest-js/README.md
./frontend/node_modules/@supabase/realtime-js/AGENTS.md
./frontend/node_modules/@supabase/realtime-js/migrations/httpsend-server-version.md
./frontend/node_modules/@supabase/realtime-js/migrations/README.md
./frontend/node_modules/@supabase/realtime-js/README.md
./frontend/node_modules/@supabase/storage-js/AGENTS.md
./frontend/node_modules/@supabase/storage-js/migrations/README.md
./frontend/node_modules/@supabase/storage-js/README.md
./frontend/node_modules/@supabase/supabase-js/AGENTS.md
./frontend/node_modules/@supabase/supabase-js/migrations/README.md
./frontend/node_modules/@supabase/supabase-js/README.md
./frontend/node_modules/@types/babel__core/README.md
./frontend/node_modules/@types/babel__generator/README.md
./frontend/node_modules/@types/babel__template/README.md
./frontend/node_modules/@types/babel__traverse/README.md
./frontend/node_modules/@types/d3-color/README.md
./frontend/node_modules/@types/d3-drag/README.md
./frontend/node_modules/@types/d3-interpolate/README.md
./frontend/node_modules/@types/d3-selection/README.md
./frontend/node_modules/@types/d3-transition/README.md
./frontend/node_modules/@types/d3-zoom/README.md
./frontend/node_modules/@types/debug/README.md
./frontend/node_modules/@types/estree/README.md
./frontend/node_modules/@types/estree-jsx/README.md
./frontend/node_modules/@types/hast/README.md
./frontend/node_modules/@types/mdast/README.md
./frontend/node_modules/@types/ms/README.md
./frontend/node_modules/@types/node/README.md
./frontend/node_modules/@types/pako/README.md
./frontend/node_modules/@types/raf/README.md
./frontend/node_modules/@types/react/README.md
./frontend/node_modules/@types/trusted-types/README.md
./frontend/node_modules/@types/unist/README.md
./frontend/node_modules/@ungap/structured-clone/README.md
./frontend/node_modules/@vercel/edge/README.md
./frontend/node_modules/@vitejs/plugin-react/README.md
./frontend/node_modules/@xyflow/react/README.md
./frontend/node_modules/@xyflow/system/README.md
./frontend/node_modules/adler-32/README.md
./frontend/node_modules/any-promise/README.md
./frontend/node_modules/anymatch/README.md
./frontend/node_modules/arg/LICENSE.md
./frontend/node_modules/arg/README.md
./frontend/node_modules/autoprefixer/README.md
./frontend/node_modules/bail/readme.md
./frontend/node_modules/base64-arraybuffer/CHANGELOG.md
./frontend/node_modules/base64-arraybuffer/README.md
./frontend/node_modules/baseline-browser-mapping/README.md
./frontend/node_modules/binary-extensions/readme.md
./frontend/node_modules/braces/README.md
./frontend/node_modules/browserslist/README.md
./frontend/node_modules/camelcase-css/README.md
./frontend/node_modules/caniuse-lite/README.md
./frontend/node_modules/canvg/README.md
./frontend/node_modules/ccount/readme.md
./frontend/node_modules/cfb/README.md
./frontend/node_modules/character-entities/readme.md
./frontend/node_modules/character-entities-html4/readme.md
./frontend/node_modules/character-entities-legacy/readme.md
./frontend/node_modules/character-reference-invalid/readme.md
./frontend/node_modules/chokidar/node_modules/glob-parent/CHANGELOG.md
./frontend/node_modules/chokidar/node_modules/glob-parent/README.md
./frontend/node_modules/chokidar/README.md
./frontend/node_modules/classcat/LICENSE.md
./frontend/node_modules/classcat/README.md
./frontend/node_modules/codepage/README.md
./frontend/node_modules/comma-separated-tokens/readme.md
./frontend/node_modules/commander/CHANGELOG.md
./frontend/node_modules/commander/Readme.md
./frontend/node_modules/convert-source-map/README.md
./frontend/node_modules/cookie/README.md
./frontend/node_modules/core-js/actual/README.md
./frontend/node_modules/core-js/es/README.md
./frontend/node_modules/core-js/full/README.md
./frontend/node_modules/core-js/internals/README.md
./frontend/node_modules/core-js/modules/README.md
./frontend/node_modules/core-js/README.md
./frontend/node_modules/core-js/stable/README.md
./frontend/node_modules/core-js/stage/README.md
./frontend/node_modules/core-js/web/README.md
./frontend/node_modules/core-util-is/README.md
./frontend/node_modules/crc-32/README.md
./frontend/node_modules/css-line-break/CHANGELOG.md
./frontend/node_modules/css-line-break/README.md
./frontend/node_modules/cssesc/README.md
./frontend/node_modules/csstype/README.md
./frontend/node_modules/d3-array/README.md
./frontend/node_modules/d3-color/README.md
./frontend/node_modules/d3-dispatch/README.md
./frontend/node_modules/d3-drag/README.md
./frontend/node_modules/d3-ease/README.md
./frontend/node_modules/d3-format/README.md
./frontend/node_modules/d3-geo/node_modules/d3-array/README.md
./frontend/node_modules/d3-geo/node_modules/internmap/README.md
./frontend/node_modules/d3-geo/README.md
./frontend/node_modules/d3-interpolate/README.md
./frontend/node_modules/d3-scale/README.md
./frontend/node_modules/d3-selection/README.md
./frontend/node_modules/d3-time/README.md
./frontend/node_modules/d3-time-format/README.md
./frontend/node_modules/d3-timer/README.md
./frontend/node_modules/d3-transition/README.md
./frontend/node_modules/d3-zoom/README.md
./frontend/node_modules/debug/README.md
./frontend/node_modules/decode-named-character-reference/readme.md
./frontend/node_modules/dequal/readme.md
./frontend/node_modules/devlop/readme.md
./frontend/node_modules/didyoumean/README.md
./frontend/node_modules/dlv/README.md
./frontend/node_modules/dompurify/README.md
./frontend/node_modules/electron-to-chromium/README.md
./frontend/node_modules/esbuild/LICENSE.md
./frontend/node_modules/esbuild/README.md
./frontend/node_modules/escalade/readme.md
./frontend/node_modules/escape-string-regexp/readme.md
./frontend/node_modules/estree-util-is-identifier-name/readme.md
./frontend/node_modules/extend/CHANGELOG.md
./frontend/node_modules/extend/README.md
./frontend/node_modules/fast-glob/node_modules/glob-parent/CHANGELOG.md
./frontend/node_modules/fast-glob/node_modules/glob-parent/README.md
./frontend/node_modules/fast-glob/README.md
./frontend/node_modules/fast-png/README.md
./frontend/node_modules/fastq/README.md
./frontend/node_modules/fastq/SECURITY.md
./frontend/node_modules/fflate/CHANGELOG.md
./frontend/node_modules/fflate/README.md
./frontend/node_modules/fill-range/README.md
./frontend/node_modules/frac/README.md
./frontend/node_modules/fraction.js/CHANGELOG.md
./frontend/node_modules/fraction.js/README.md
./frontend/node_modules/function-bind/.github/SECURITY.md
./frontend/node_modules/function-bind/CHANGELOG.md
./frontend/node_modules/function-bind/README.md
./frontend/node_modules/gensync/README.md
./frontend/node_modules/glob-parent/README.md
./frontend/node_modules/hasown/CHANGELOG.md
./frontend/node_modules/hasown/README.md
./frontend/node_modules/hast-util-to-jsx-runtime/readme.md
./frontend/node_modules/hast-util-whitespace/readme.md
./frontend/node_modules/html-url-attributes/readme.md
./frontend/node_modules/html2canvas/CHANGELOG.md
./frontend/node_modules/html2canvas/README.md
./frontend/node_modules/iceberg-js/README.md
./frontend/node_modules/image-size/Readme.md
./frontend/node_modules/immediate/README.md
./frontend/node_modules/inherits/README.md
./frontend/node_modules/inline-style-parser/README.md
./frontend/node_modules/internmap/README.md
./frontend/node_modules/iobuffer/README.md
./frontend/node_modules/is-alphabetical/readme.md
./frontend/node_modules/is-alphanumerical/readme.md
./frontend/node_modules/is-binary-path/readme.md
./frontend/node_modules/is-core-module/CHANGELOG.md
./frontend/node_modules/is-core-module/README.md
./frontend/node_modules/is-decimal/readme.md
./frontend/node_modules/is-extglob/README.md
./frontend/node_modules/is-glob/README.md
./frontend/node_modules/is-hexadecimal/readme.md
./frontend/node_modules/is-number/README.md
./frontend/node_modules/is-plain-obj/readme.md
./frontend/node_modules/isarray/README.md
./frontend/node_modules/jiti/README.md
./frontend/node_modules/jose/LICENSE.md
./frontend/node_modules/jose/README.md
./frontend/node_modules/js-tokens/CHANGELOG.md
./frontend/node_modules/js-tokens/README.md
./frontend/node_modules/jsesc/README.md
./frontend/node_modules/json5/LICENSE.md
./frontend/node_modules/json5/README.md
./frontend/node_modules/jspdf/README.md
./frontend/node_modules/jspdf-autotable/README.md
./frontend/node_modules/jszip/CHANGES.md
./frontend/node_modules/jszip/node_modules/pako/CHANGELOG.md
./frontend/node_modules/jszip/node_modules/pako/README.md
./frontend/node_modules/jszip/sponsors.md
./frontend/node_modules/lie/license.md
./frontend/node_modules/lie/README.md
./frontend/node_modules/lilconfig/readme.md
./frontend/node_modules/lines-and-columns/README.md
./frontend/node_modules/longest-streak/readme.md
./frontend/node_modules/loose-envify/README.md
./frontend/node_modules/lru-cache/README.md
./frontend/node_modules/lucide-react/README.md
./frontend/node_modules/markdown-table/readme.md
./frontend/node_modules/mdast-util-find-and-replace/readme.md
./frontend/node_modules/mdast-util-from-markdown/readme.md
./frontend/node_modules/mdast-util-gfm/readme.md
./frontend/node_modules/mdast-util-gfm-autolink-literal/readme.md
./frontend/node_modules/mdast-util-gfm-footnote/readme.md
./frontend/node_modules/mdast-util-gfm-strikethrough/readme.md
./frontend/node_modules/mdast-util-gfm-table/readme.md
./frontend/node_modules/mdast-util-gfm-task-list-item/readme.md
./frontend/node_modules/mdast-util-mdx-expression/readme.md
./frontend/node_modules/mdast-util-mdx-jsx/readme.md
./frontend/node_modules/mdast-util-mdxjs-esm/readme.md
./frontend/node_modules/mdast-util-phrasing/readme.md
./frontend/node_modules/mdast-util-to-hast/readme.md
./frontend/node_modules/mdast-util-to-markdown/readme.md
./frontend/node_modules/mdast-util-to-string/readme.md
./frontend/node_modules/merge2/README.md
./frontend/node_modules/micromark/readme.md
./frontend/node_modules/micromark-core-commonmark/readme.md
./frontend/node_modules/micromark-extension-gfm/readme.md
./frontend/node_modules/micromark-extension-gfm-autolink-literal/readme.md
./frontend/node_modules/micromark-extension-gfm-footnote/readme.md
./frontend/node_modules/micromark-extension-gfm-strikethrough/readme.md
./frontend/node_modules/micromark-extension-gfm-table/readme.md
./frontend/node_modules/micromark-extension-gfm-tagfilter/readme.md
./frontend/node_modules/micromark-extension-gfm-task-list-item/readme.md
./frontend/node_modules/micromark-factory-destination/readme.md
./frontend/node_modules/micromark-factory-label/readme.md
./frontend/node_modules/micromark-factory-space/readme.md
./frontend/node_modules/micromark-factory-title/readme.md
./frontend/node_modules/micromark-factory-whitespace/readme.md
./frontend/node_modules/micromark-util-character/readme.md
./frontend/node_modules/micromark-util-chunked/readme.md
./frontend/node_modules/micromark-util-classify-character/readme.md
./frontend/node_modules/micromark-util-combine-extensions/readme.md
./frontend/node_modules/micromark-util-decode-numeric-character-reference/readme.md
./frontend/node_modules/micromark-util-decode-string/readme.md
./frontend/node_modules/micromark-util-encode/readme.md
./frontend/node_modules/micromark-util-html-tag-name/readme.md
./frontend/node_modules/micromark-util-normalize-identifier/readme.md
./frontend/node_modules/micromark-util-resolve-all/readme.md
./frontend/node_modules/micromark-util-sanitize-uri/readme.md
./frontend/node_modules/micromark-util-subtokenize/readme.md
./frontend/node_modules/micromark-util-symbol/readme.md
./frontend/node_modules/micromark-util-types/readme.md
./frontend/node_modules/micromatch/README.md
./frontend/node_modules/ms/license.md
./frontend/node_modules/ms/readme.md
./frontend/node_modules/mz/HISTORY.md
./frontend/node_modules/mz/README.md
./frontend/node_modules/nanoid/README.md
./frontend/node_modules/node-releases/README.md
./frontend/node_modules/normalize-path/README.md
./frontend/node_modules/object-assign/readme.md
./frontend/node_modules/pako/README.md
./frontend/node_modules/parse-entities/node_modules/@types/unist/README.md
./frontend/node_modules/parse-entities/readme.md
./frontend/node_modules/path-parse/README.md
./frontend/node_modules/performance-now/README.md
./frontend/node_modules/picocolors/README.md
./frontend/node_modules/picomatch/README.md
./frontend/node_modules/pify/readme.md
./frontend/node_modules/pirates/README.md
./frontend/node_modules/postcss/README.md
./frontend/node_modules/postcss-import/README.md
./frontend/node_modules/postcss-js/README.md
./frontend/node_modules/postcss-load-config/README.md
./frontend/node_modules/postcss-nested/README.md
./frontend/node_modules/postcss-selector-parser/API.md
./frontend/node_modules/postcss-selector-parser/CHANGELOG.md
./frontend/node_modules/postcss-selector-parser/README.md
./frontend/node_modules/postcss-value-parser/README.md
./frontend/node_modules/pptxgenjs/README.md
./frontend/node_modules/process-nextick-args/license.md
./frontend/node_modules/process-nextick-args/readme.md
./frontend/node_modules/prop-types/README.md
./frontend/node_modules/property-information/readme.md
./frontend/node_modules/queue/readme.md
./frontend/node_modules/queue-microtask/README.md
./frontend/node_modules/raf/README.md
./frontend/node_modules/react/README.md
./frontend/node_modules/react-dom/README.md
./frontend/node_modules/react-is/README.md
./frontend/node_modules/react-markdown/readme.md
./frontend/node_modules/react-refresh/README.md
./frontend/node_modules/react-router/CHANGELOG.md
./frontend/node_modules/react-router/LICENSE.md
./frontend/node_modules/react-router/README.md
./frontend/node_modules/react-router-dom/LICENSE.md
./frontend/node_modules/react-router-dom/README.md
./frontend/node_modules/react-simple-maps/node_modules/d3-color/README.md
./frontend/node_modules/react-simple-maps/node_modules/d3-dispatch/README.md
./frontend/node_modules/react-simple-maps/node_modules/d3-drag/README.md
./frontend/node_modules/react-simple-maps/node_modules/d3-ease/README.md
./frontend/node_modules/react-simple-maps/node_modules/d3-interpolate/README.md
./frontend/node_modules/react-simple-maps/node_modules/d3-selection/README.md
./frontend/node_modules/react-simple-maps/node_modules/d3-timer/README.md
./frontend/node_modules/react-simple-maps/node_modules/d3-transition/README.md
./frontend/node_modules/react-simple-maps/node_modules/d3-zoom/README.md
./frontend/node_modules/react-simple-maps/README.md
./frontend/node_modules/read-cache/README.md
./frontend/node_modules/readable-stream/CONTRIBUTING.md
./frontend/node_modules/readable-stream/doc/wg-meetings/2015-01-30.md
./frontend/node_modules/readable-stream/GOVERNANCE.md
./frontend/node_modules/readable-stream/README.md
./frontend/node_modules/readdirp/README.md
./frontend/node_modules/regenerator-runtime/README.md
./frontend/node_modules/remark-gfm/readme.md
./frontend/node_modules/remark-parse/readme.md
./frontend/node_modules/remark-rehype/readme.md
./frontend/node_modules/remark-stringify/readme.md
./frontend/node_modules/resolve/.github/INCIDENT_RESPONSE_PROCESS.md
./frontend/node_modules/resolve/.github/THREAT_MODEL.md
./frontend/node_modules/resolve/SECURITY.md
./frontend/node_modules/reusify/README.md
./frontend/node_modules/reusify/SECURITY.md
./frontend/node_modules/rgbcolor/FEEL-FREE.md
./frontend/node_modules/rgbcolor/LICENSE.md
./frontend/node_modules/rgbcolor/README.md
./frontend/node_modules/rollup/LICENSE.md
./frontend/node_modules/rollup/README.md
./frontend/node_modules/run-parallel/README.md
./frontend/node_modules/safe-buffer/README.md
./frontend/node_modules/scheduler/README.md
./frontend/node_modules/semver/README.md
./frontend/node_modules/set-cookie-parser/README.md
./frontend/node_modules/simple-icons/DISCLAIMER.md
./frontend/node_modules/simple-icons/LICENSE.md
./frontend/node_modules/simple-icons/README.md
./frontend/node_modules/simple-icons/VERSIONING.md
./frontend/node_modules/source-map-js/README.md
./frontend/node_modules/space-separated-tokens/readme.md
./frontend/node_modules/ssf/README.md
./frontend/node_modules/stackblur-canvas/CHANGES.md
./frontend/node_modules/stackblur-canvas/README.md
./frontend/node_modules/stringify-entities/readme.md
./frontend/node_modules/string_decoder/README.md
./frontend/node_modules/style-to-js/README.md
./frontend/node_modules/style-to-object/README.md
./frontend/node_modules/sucrase/README.md
./frontend/node_modules/supports-preserve-symlinks-flag/CHANGELOG.md
./frontend/node_modules/supports-preserve-symlinks-flag/README.md
./frontend/node_modules/svg-pathdata/CHANGELOG.md
./frontend/node_modules/svg-pathdata/README.md
./frontend/node_modules/tailwindcss/lib/postcss-plugins/nesting/README.md
./frontend/node_modules/tailwindcss/lib/value-parser/README.md
./frontend/node_modules/tailwindcss/README.md
./frontend/node_modules/tailwindcss/src/postcss-plugins/nesting/README.md
./frontend/node_modules/tailwindcss/src/value-parser/README.md
./frontend/node_modules/text-segmentation/CHANGELOG.md
./frontend/node_modules/text-segmentation/README.md
./frontend/node_modules/thenify/History.md
./frontend/node_modules/thenify/README.md
./frontend/node_modules/thenify-all/History.md
./frontend/node_modules/thenify-all/README.md
./frontend/node_modules/tinyglobby/node_modules/fdir/README.md
./frontend/node_modules/tinyglobby/node_modules/picomatch/README.md
./frontend/node_modules/tinyglobby/README.md
./frontend/node_modules/to-regex-range/README.md
./frontend/node_modules/topojson-client/node_modules/commander/CHANGELOG.md
./frontend/node_modules/topojson-client/node_modules/commander/Readme.md
./frontend/node_modules/topojson-client/README.md
./frontend/node_modules/trim-lines/readme.md
./frontend/node_modules/trough/readme.md
./frontend/node_modules/ts-interface-checker/README.md
./frontend/node_modules/tslib/README.md
./frontend/node_modules/tslib/SECURITY.md
./frontend/node_modules/undici-types/README.md
./frontend/node_modules/unified/readme.md
./frontend/node_modules/unist-util-is/readme.md
./frontend/node_modules/unist-util-position/readme.md
./frontend/node_modules/unist-util-stringify-position/readme.md
./frontend/node_modules/unist-util-visit/readme.md
./frontend/node_modules/unist-util-visit-parents/readme.md
./frontend/node_modules/update-browserslist-db/README.md
./frontend/node_modules/us-atlas/README.md
./frontend/node_modules/use-sync-external-store/README.md
./frontend/node_modules/util-deprecate/History.md
./frontend/node_modules/util-deprecate/README.md
./frontend/node_modules/utrie/CHANGELOG.md
./frontend/node_modules/vfile/readme.md
./frontend/node_modules/vfile-message/readme.md
./frontend/node_modules/vite/LICENSE.md
./frontend/node_modules/vite/README.md
./frontend/node_modules/wmf/README.md
./frontend/node_modules/word/CONTRIBUTING.md
./frontend/node_modules/word/README.md
./frontend/node_modules/xlsx/CHANGELOG.md
./frontend/node_modules/xlsx/README.md
./frontend/node_modules/yallist/README.md
./frontend/node_modules/zustand/readme.md
./frontend/node_modules/zwitch/readme.md
./frontend/README.md
./libs/agno/egpt/db/README.md
./libs/agno/egpt/integrations/db/clickhouse/README.md
./libs/agno/migrations/README.md
./libs/agno/README.md
./libs/agno/tests/COVERAGE_BASELINE.md
./libs/agno/tests/integration/knowledge/data/filters/cv_1.md
./libs/agno/tests/integration/knowledge/data/filters/cv_2.md
./libs/agno/tests/integration/knowledge/data/pg_essay.md
./libs/agno/tests/integration/models/litellm_openai/README.md
./libs/agno/tests/system/README.md
./libs/agno_infra/README.md
./libs/egptctl/README.md
./product/.pytest_cache/README.md
./product/egpt_retail/api/openapi/CHANGELOG.md
./product/egpt_retail/contracts/CHANGELOG.md
./product/egpt_retail/contracts/EXECUTOR_REGISTRY.md
./product/egpt_retail/contracts/LANDING_CONTRACT.md
./product/egpt_retail/contracts/MEMORY_SCOPE.md
./product/egpt_retail/contracts/_fixtures/landing/README.md
./product/egpt_retail/contracts/_fixtures/README.md
./product/egpt_retail/knowledge/corpus/00-table-of-contents.md
./product/egpt_retail/knowledge/corpus/01-retail-fundamentals-and-terminology.md
./product/egpt_retail/knowledge/corpus/02-customer-fundamentals-and-shopper-psychology.md
./product/egpt_retail/knowledge/corpus/03-merchandising-and-visual-merchandising.md
./product/egpt_retail/knowledge/corpus/04-category-management.md
./product/egpt_retail/knowledge/corpus/05-pricing-strategy-and-promotions.md
./product/egpt_retail/knowledge/corpus/06-private-label-and-own-brand-strategy.md
./product/egpt_retail/knowledge/corpus/07-supply-chain-and-logistics.md
./product/egpt_retail/knowledge/corpus/08-inventory-management-and-demand-forecasting.md
./product/egpt_retail/knowledge/corpus/09-store-design-and-real-estate.md
./product/egpt_retail/knowledge/corpus/10-store-operations-and-workforce-management.md
./product/egpt_retail/knowledge/corpus/11-ecommerce-and-digital-commerce.md
./product/egpt_retail/knowledge/corpus/12-omnichannel-and-unified-commerce.md
./product/egpt_retail/knowledge/corpus/13-emerging-commerce-models.md
./product/egpt_retail/knowledge/corpus/14-retail-marketing-and-loyalty-programs.md
./product/egpt_retail/knowledge/corpus/15-retail-media-networks.md
./product/egpt_retail/knowledge/corpus/16-retail-technology-and-core-systems.md
./product/egpt_retail/knowledge/corpus/17-emerging-technology-in-retail.md
./product/egpt_retail/knowledge/corpus/18-retail-analytics-and-data-infrastructure.md
./product/egpt_retail/knowledge/corpus/19-ai-ml-use-cases-in-retail.md
./product/egpt_retail/knowledge/corpus/20-customer-research-and-insights.md
./product/egpt_retail/knowledge/corpus/21-post-purchase-and-customer-service.md
./product/egpt_retail/knowledge/corpus/22-finance-and-unit-economics.md
./product/egpt_retail/knowledge/corpus/23-vendor-and-supplier-management.md
./product/egpt_retail/knowledge/corpus/24-payments-fraud-and-financial-services.md
./product/egpt_retail/knowledge/corpus/25-retail-verticals-deep-dive.md
./product/egpt_retail/knowledge/corpus/26-franchising-and-wholesale-b2b-retail.md
./product/egpt_retail/knowledge/corpus/27-international-retail-and-localization.md
./product/egpt_retail/knowledge/corpus/28-regulatory-compliance-and-sustainability.md
./product/egpt_retail/knowledge/corpus/29-competitive-landscape-and-industry-frameworks.md
./product/egpt_retail/knowledge/corpus/30-retail-strategy-and-future-trends.md
./product/egpt_retail/knowledge/corpus/31-crisis-and-risk-management-in-retail.md
./product/egpt_retail/knowledge/corpus/README.md
./product/egpt_retail/kpi/README.md
./product/egpt_retail/skills/at_risk_explanation.md
./product/egpt_retail/skills/dashboard_suggestion.md
./product/egpt_retail/skills/diagnosis_explanation.md
./product/egpt_retail/skills/enrichment_proposer.md
./product/egpt_retail/skills/EXAMPLE.md
./product/egpt_retail/skills/funnel_explanation.md
./product/egpt_retail/skills/join_path_explainer.md
./product/egpt_retail/skills/kpi_suggestion.md
./product/egpt_retail/skills/mapping_proposer.md
./product/egpt_retail/skills/playground.md
./product/egpt_retail/skills/report_explanation.md
./product/egpt_retail/skills/SKILL_TEMPLATE.md
./product/egpt_retail/skills/spec_extractor.md
./product/egpt_retail/skills/step_prompt.md
./product/egpt_retail/skills/use_case_suggestion.md
./product/egpt_retail/warehouse/LOAD_CONTRACT.md
./product/README.md
./PROVENANCE.md
./README.md
./scripts/templates/README.md

-> Locates files by name or type.

9. echo command

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ echo $PATH
/c/Saturam/saturam-agent-framework/.venv/Scripts:/c/Users/Orcon/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/Orcon/bin:/c/Program Files/Microsoft SDKs/Azure/CLI2/wbin:/c/Program Files/Common Files/Oracle/Java/javapath:/c/WINDOWS/system32:/c/WINDOWS:/c/WINDOWS/System32/Wbem:/c/WINDOWS/System32/WindowsPowerShell/v1.0:/c/WINDOWS/System32/OpenSSH:/c/Program Files/MySQL/MySQL Server 8.0/bin:/cmd:/c/Program Files/Terraform:/c/spark/spark-3.5.6-bin-hadoop3/bin:/c/hadoop/bin:/c/hadoop/bin:/c/Program Files/Java/jdk-17/bin:/c/Program Files/Java/jdk-17:/c/Program Files/Docker/Docker/resources/bin:/c/SonarQube/sonar-scanner-7.2.0.5079-windows-x64/bin:/c/kafka/kafka_2.13-3.7.0/bin:/c/Kube:/c/ProgramData/chocolatey/bin:%NVM_HOME%:%NVM_SYMLINK%:/c/Program Files/Kubernetes/Minikube:/c/Program Files/Amazon/AWSCLIV2:/c/Program Files/WSL:/c/Program Files/nodejs:/c/Users/Orcon/AppData/Local/Programs/Python/Python312/Scripts:/c/Users/Orcon/AppData/Local/Programs/Python/Python312:/c/Users/Orcon/AppData/Local/Programs/Python/Python310/Scripts:/c/Users/Orcon/AppData/Local/Programs/Python/Python310:/c/Program Files/MySQL/MySQL Shell 8.0/bin:/c/Users/Orcon/AppData/Local/Programs/Python/Launcher:/c/Users/Orcon/AppData/Local/Microsoft/WindowsApps:/c/Users/Orcon/AppData/Local/Programs/Microsoft VS Code/bin:/c/Users/Orcon/Google CLoud SDK/google-cloud-sdk/bin:/c/Users/Orcon/AppData/Local/Microsoft/WinGet/Links:/c/Users/Orcon/AppData/Local/Programs/Microsoft VS Code/bin/copilot-shim:/c/Users/Orcon/AppData/Roaming/npm:/usr/bin/vendor_perl:/usr/bin/core_perl

-> Prints text or variables to the screen.

10. which command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ which bash
/usr/bin/bash

-> Shows the exact installation path of a program.

11. export command

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ export DEMO_VAR="Hello Data Engineering"

-> Creates or sets an environment variable.

12. env command

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ env | grep DEMO_VAR
DEMO_VAR=Hello Data Engineering

-> Lists all active environment variables.


(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ ls -la | grep "README"
-rw-r--r-- 1 SMS 197121  3175 Oct 22 09:42 README.md

-> ls -la listed every single single file
-> Using pipe, it will filtered only reaadme named files.


13. cat command

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ cat README.md | wc -l > line_count.txt

-> Reads and outputs the entire contents of a file.

-> cat reads the entire readme.md file
-> Then using wc command, it will counted the number of lines.
-> Stored it in the line_count.txt and overwrite it.

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ echo "Finished terminal tasks" >> line_count.txt

-> The echo command generated the text string. The double redirect (>>) took that text and appended it to the very bottom of line_count.txt.

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ cat line_count.txt
79
Finished terminal tasks
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)

-> It printed the final contents of the file to your screen. You saw 79 on the first line and Finished terminal tasks on the second line, proving that both your overwrite (>) and your append (>>) worked perfectly.