import argparse
import os
from modules.paths_internal import data_path

parser = argparse.ArgumentParser(description="SD.Next", conflict_handler='resolve', epilog='For other options see UI Settings page', prog='', add_help=True, formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=55, indent_increment=2, width=200))
parser._optionals = parser.add_argument_group('Other options') # pylint: disable=protected-access
group = parser.add_argument_group('Server options')

# main server args
group.add_argument("--config", type=str, default=os.path.join(data_path, 'config.json'), help="Use specific server configuration file, default: %(default)s")
group.add_argument("--ui-config", type=str, default=os.path.join(data_path, 'ui-config.json'), help="Use specific UI configuration file, default: %(default)s")
group.add_argument("--medvram", action='store_true', help="Split model stages and keep only active part in VRAM, default: %(default)s")
group.add_argument("--lowvram", action='store_true', help="Split model components and keep only active part in VRAM, default: %(default)s")
group.add_argument("--ckpt", type=str, default=None, help="Path to model checkpoint to load immediately, default: %(default)s")
group.add_argument('--vae', type=str, default=None, help='Path to VAE checkpoint to load immediately, default: %(default)s')
group.add_argument("--data-dir", type=str, default=os.path.dirname(os.path.dirname(os.path.realpath(__file__))), help="Base path where all user data is stored, default: %(default)s")
group.add_argument("--models-dir", type=str, default="models", help="Base path where all models are stored, default: %(default)s",)
group.add_argument("--allow-code", action='store_true', help="Allow custom script execution, default: %(default)s")
group.add_argument("--share", action='store_true', help="Enable UI accessible through Gradio site, default: %(default)s")
group.add_argument("--insecure", action='store_true', help="Enable extensions tab regardless of other options, default: %(default)s")
group.add_argument("--use-cpu", nargs='+', default=[], type=str.lower, help="Force use CPU for specified modules, default: %(default)s")
group.add_argument("--listen", action='store_true', help="Launch web server using public IP address, default: %(default)s")
group.add_argument("--port", type=int, default=7860, help="Launch web server with given server port, default: %(default)s")
group.add_argument("--freeze", action='store_true', help="Disable editing settings", default=False)
group.add_argument("--auth", type=str, help='Set access authentication like "user:pwd,user:pwd""', default=None)
group.add_argument("--auth-file", type=str, help='Set access authentication using file, default: %(default)s', default=None)
group.add_argument("--autolaunch", action='store_true', help="Open the UI URL in the system's default browser upon launch", default=False)
group.add_argument('--api-only', default = False, action='store_true', help = "Run in API only mode without starting UI")
group.add_argument("--api-log", default=False, action='store_true', help="Enable logging of all API requests, default: %(default)s")
group.add_argument("--device-id", type=str, help="Select the default CUDA device to use, default: %(default)s", default=None)
group.add_argument("--cors-origins", type=str, help="Allowed CORS origins as comma-separated list, default: %(default)s", default=None)
group.add_argument("--cors-regex", type=str, help="Allowed CORS origins as regular expression, default: %(default)s", default=None)
group.add_argument("--tls-keyfile", type=str, help="Enable TLS and specify key file, default: %(default)s", default=None)
group.add_argument("--tls-certfile", type=str, help="Enable TLS and specify cert file, default: %(default)s", default=None)
group.add_argument("--tls-selfsign", action="store_true", help="Enable TLS with self-signed certificates, default: %(default)s", default=None)
group.add_argument("--server-name", type=str, help="Sets hostname of server, default: %(default)s", default=None)
group.add_argument("--no-hashing", action='store_true', help="Disable hashing of checkpoints, default: %(default)s", default=False)
group.add_argument("--no-download", action='store_true', help="Disable download of default model, default: %(default)s", default=False)
group.add_argument("--profile", action='store_true', help="Run profiler, default: %(default)s")
group.add_argument("--disable-queue", action='store_true', help="Disable queues, default: %(default)s")
group.add_argument('--debug', default = False, action='store_true', help = "Run installer with debug logging, default: %(default)s")
group.add_argument("--use-ipex", default = False, action='store_true', help="Use Intel OneAPI XPU backend, default: %(default)s")
group.add_argument('--use-directml', default = False, action='store_true', help = "Use DirectML if no compatible GPU is detected, default: %(default)s")
group.add_argument("--use-cuda", default=False, action='store_true', help="Force use nVidia CUDA backend, default: %(default)s")
group.add_argument("--use-rocm", default=False, action='store_true', help="Force use AMD ROCm backend, default: %(default)s")
group.add_argument('--subpath', type=str, help='Customize the URL subpath for usage with reverse proxy')
group.add_argument('--backend', type=str, choices=[None, 'original', 'diffusers'], default=None, required=False, help='force backend type')
parser.add_argument("--cloudflared", action="store_true", help="use trycloudflare, alternative to gradio --share")


# removed args are added here as hidden in fixed format for compatbility reasons
group.add_argument("-f", action='store_true', help=argparse.SUPPRESS)  # allows running as root; implemented outside of webui
group.add_argument("--ui-settings-file", type=str, help=argparse.SUPPRESS, default=os.path.join(data_path, 'config.json'))
group.add_argument("--ui-config-file", type=str, help=argparse.SUPPRESS, default=os.path.join(data_path, 'ui-config.json'))
group.add_argument("--hide-ui-dir-config", action='store_true', help=argparse.SUPPRESS, default=False)
group.add_argument("--theme", type=str, help=argparse.SUPPRESS, default=None)
group.add_argument("--disable-console-progressbars", action='store_true', help=argparse.SUPPRESS, default=True)
group.add_argument("--disable-safe-unpickle", action='store_true', help=argparse.SUPPRESS, default=True)
group.add_argument("--lowram", action='store_true', help=argparse.SUPPRESS)
group.add_argument("--disable-extension-access", default = False, action='store_true', help=argparse.SUPPRESS)
group.add_argument("--api", help=argparse.SUPPRESS, default=True)
group.add_argument("--api-auth", type=str, help=argparse.SUPPRESS, default=None)


def compatibility_args(opts, args):
    # removed args that have been moved to opts are added here as hidden with default values as defined in opts
    group.add_argument("--ckpt-dir", type=str, help=argparse.SUPPRESS, default=opts.ckpt_dir)
    group.add_argument("--vae-dir", type=str, help=argparse.SUPPRESS, default=opts.vae_dir)
    group.add_argument("--embeddings-dir", type=str, help=argparse.SUPPRESS, default=opts.embeddings_dir)
    group.add_argument("--embeddings-templates-dir", type=str, help=argparse.SUPPRESS, default=opts.embeddings_templates_dir)
    group.add_argument("--hypernetwork-dir", type=str, help=argparse.SUPPRESS, default=opts.hypernetwork_dir)
    group.add_argument("--codeformer-models-path", type=str, help=argparse.SUPPRESS, default=opts.codeformer_models_path)
    group.add_argument("--gfpgan-models-path", type=str, help=argparse.SUPPRESS, default=opts.gfpgan_models_path)
    group.add_argument("--esrgan-models-path", type=str, help=argparse.SUPPRESS, default=opts.esrgan_models_path)
    group.add_argument("--bsrgan-models-path", type=str, help=argparse.SUPPRESS, default=opts.bsrgan_models_path)
    group.add_argument("--realesrgan-models-path", type=str, help=argparse.SUPPRESS, default=opts.realesrgan_models_path)
    group.add_argument("--scunet-models-path", help=argparse.SUPPRESS, default=opts.scunet_models_path)
    group.add_argument("--swinir-models-path", help=argparse.SUPPRESS, default=opts.swinir_models_path)
    group.add_argument("--ldsr-models-path", help=argparse.SUPPRESS, default=opts.ldsr_models_path)
    group.add_argument("--clip-models-path", type=str, help=argparse.SUPPRESS, default=opts.clip_models_path)
    group.add_argument("--opt-channelslast", help=argparse.SUPPRESS, default=opts.opt_channelslast)
    group.add_argument("--xformers", default = (opts.cross_attention_optimization == "xFormers"), action='store_true', help=argparse.SUPPRESS)
    group.add_argument("--disable-nan-check", help=argparse.SUPPRESS, default=opts.disable_nan_check)
    group.add_argument("--token-merging", help=argparse.SUPPRESS, default=opts.token_merging)
    group.add_argument("--rollback-vae", help=argparse.SUPPRESS, default=opts.rollback_vae)
    group.add_argument("--no-half", help=argparse.SUPPRESS, default=opts.no_half)
    group.add_argument("--no-half-vae", help=argparse.SUPPRESS, default=opts.no_half_vae)
    group.add_argument("--precision", help=argparse.SUPPRESS, default=opts.precision)
    group.add_argument("--sub-quad-q-chunk-size", help=argparse.SUPPRESS, default=opts.sub_quad_q_chunk_size)
    group.add_argument("--sub-quad-kv-chunk-size", help=argparse.SUPPRESS, default=opts.sub_quad_kv_chunk_size)
    group.add_argument("--sub-quad-chunk-threshold", help=argparse.SUPPRESS, default=opts.sub_quad_chunk_threshold)
    group.add_argument("--lora-dir", help=argparse.SUPPRESS, default=opts.lora_dir)
    group.add_argument("--lyco-dir", help=argparse.SUPPRESS, default=opts.lyco_dir)
    group.add_argument("--enable-console-prompts", help=argparse.SUPPRESS, action='store_true', default=False)
    group.add_argument("--safe", help=argparse.SUPPRESS, action='store_true', default=False)

    # removed opts are added here with fixed values for compatibility reasons
    opts.use_old_emphasis_implementation = False
    opts.use_old_karras_scheduler_sigmas = False
    opts.no_dpmpp_sde_batch_determinism = False
    opts.lora_apply_to_outputs = False
    opts.do_not_show_images = False
    opts.add_model_hash_to_info = True
    opts.add_model_name_to_info = True
    opts.js_modal_lightbox = True
    opts.js_modal_lightbox_initially_zoomed = True
    opts.show_progress_in_title = False
    opts.sd_vae_as_default = True
    opts.enable_emphasis = True
    opts.enable_batch_seeds = True
    opts.multiple_tqdm = False
    opts.print_hypernet_extra = False
    opts.dimensions_and_batch_together = True
    opts.enable_pnginfo = True
    opts.data['clip_skip'] = 1

    args = parser.parse_args()
    return args
