# Week 14 — Block 2 Demo Guide (~25 min): Deploy + Honesty Pass

Pre-class: pick ONE volunteer final project (arranged beforehand) with repo access,
or use your own Weeks 12-13 reference system.

## Part 1 (~15 min) — deploy the two pieces, live
1. Server -> Render/Railway (or show the already-deployed one): walk the service
   config, env vars, the /health check returning 200 from the public URL.
2. Client -> share.streamlit.io: New app -> repo -> add API_URL in Settings/Secrets.
   NARRATE THE #1 BUG: localhost hard-coding. Show the st.secrets.get(...) fallback line.
3. Open the public client. Make a live prediction. Then PAUSE the server in the host
   dashboard and reload the client -> the graceful st.error path, on the open web.

## Part 2 (~10 min) — the honesty pass, on the deployed app
Walk the four critique lenses against the live app, thinking aloud:
1. Accuracy/honesty: axis games? counts-as-rates? a confident progress bar?
2. Clarity: the 10-second test — what's the main message?
3. The loop: /health green? failure graceful? /model-info present?
4. Accessibility: palette colorblind-safe? meaning by color alone anywhere?

Then run `deployment_checklist.md` against it line by line. Two boxes will fail —
they always do. That's the point: checklists beat memory.

Hand out / point to: deployment_checklist.md, critique_sheet.md.
Block 3 runs per workshop_runsheet.md.
